# -*- coding: utf-8 -*-
import json as simplejson

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework import status#, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser

from api.permissions import UserPermission
from api.serializers import SlidePostSerializer, SlideGetSerializer, BroadcastingSerializer

from broadcasts.models import Event, Broadcasting, Slide

from api.forms import SlideForm

class Slide(APIView):
    permission_classes = (UserPermission,)
    parser_classes = (MultiPartParser,)
    
    def post(self, request,format=None):
        serializer = SlidePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SlideList(APIView):
    permission_classes = (UserPermission,)

    def get_object(self, bk):
        try:
            broadcasting = Broadcasting.objects.get(pk=int(bk))
        except Broadcasting.DoesNotExist:
            raise Http404
        except Broadcasting.MultipleObjectsReturned:
            raise Http404
        return broadcasting.slides.all()
        
    def get(self, request, bk, format=None):
        slides = self.get_object(bk)
        serializer = SlideGetSerializer(slides, many=True)
        return Response(serializer.data) 

class SlideDetail(APIView):
    permission_classes = (UserPermission,)

    def get_object(self, bk, pos):
        try:
            broadcasting = Broadcasting.objects.get(pk=int(bk))
        except Broadcasting.DoesNotExist:
            raise Http404
        except Broadcasting.MultipleObjectsReturned:
            raise Http404
        slides = broadcasting.slides.all()
        try:
            return slides.get(position=int(pos))
        except:
            raise Http404
        
    def get(self, request, bk, pos, format=None):
        slide = self.get_object(bk,pos)
        serializer = SlideGetSerializer(slide)
        return Response(serializer.data) 

class BroadcastingView(APIView):
    permission_classes = (UserPermission,)
    
    def get_object(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
        try:
            broadcasting = Broadcasting.objects.get(owner=user, active=True)
        except Broadcasting.DoesNotExist:
            return None
        except Broadcasting.MultipleObjectsReturned:
            return None
        return broadcasting
    #get info
    def get_user_id(self, request, format=None):
        user_id = user_map.user.id
        return Response(serializer.data)
        
    def get(self, request, user_id, format=None):
        broadcasting = self.get_object(user_id)
        serializer = BroadcastingSerializer(broadcasting)
        return Response(serializer.data) 
    #disable (active=False)
    def put(self, request, user_id, format=None):
        broadcasting = self.get_object(user_id)
        if broadcasting != None:
            broadcasting.active=False
            broadcasting.save()
        serializer = BroadcastingSerializer(broadcasting)
        return Response(serializer.data) 
    #create new presentation
    def post(self, request, user_id, format=None):
        broadcasting = self.get_object(user_id)
        if broadcasting != None:
            broadcasting.active=False
            broadcasting.save()
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
        
        broadcasting = Broadcasting(owner=user, active=True, title='New Slides @'+ user.username, desc='')
        broadcasting.save()
        serializer = BroadcastingSerializer(broadcasting)
        return Response(serializer.data) 
    
class CurrentBroadcasting(APIView):
    permission_classes = (UserPermission,)

    def get_object(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404
        try:
            broadcasting = Broadcasting.objects.get(owner=user, active=True)
        except Broadcasting.DoesNotExist:
            return None
        except Broadcasting.MultipleObjectsReturned:
            return None
        return broadcasting
        
    #id prezentacii po useru
    def get(self, request, user_id, format=None):
        broadcasting = self.get_object(user_id)
        if broadcasting != None: 
            return Response(broadcasting.pk)
        else:
            return Response(-1)
        
class GetUserID(APIView):
    permission_classes = (UserPermission,)

    def get_user_id(self, username, email):
        try:
            user = User.objects.get(username=username, email=email)
            return user.pk
        except User.DoesNotExist:
            return -1
        
    #id prezentacii po useru
    def get(self, request, format=None):
        username = request.query_params.get('username')
        email = request.query_params.get('email')
        userid = self.get_user_id(username, email)
        return Response(userid)
