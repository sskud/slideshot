from mercurial.dispatch import request
from django.shortcuts import render_to_response, redirect
from home.models import *
from django.template import RequestContext
from django.http import HttpResponseBadRequest, Http404, HttpResponse
from users.views import complete_registration
#import random
#from loginza.models import UserMap
#from django.core.exceptions import ObjectDoesNotExist
from django import forms

from broadcasts.models import Event, Broadcasting, Slide
from broadcasts.paginators import *

def index(request):
#    broadcastings = get_pagination_broadcastings(request, request.GET.get('brp'),10)
#    response = {'broadcastings':broadcastings}
    response = {}
    if 'users_complete_reg_id' in request.session:
        form = complete_registration(request)
        response['form'] = form

    return render_to_response('index.html', response, context_instance=RequestContext(request))

# Create your views here.
