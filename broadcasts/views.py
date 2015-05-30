# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect 
from django.template import RequestContext
from django.http import Http404, HttpResponse

from broadcasts.models import Event, Broadcasting, Slide
from broadcasts.paginators import *

#sign up and sign in or login as anonimus
#redirect to mainpage
'''def hellopage(request):
    pass
'''
#TODO: уточнить у светы, пока что ничего

def mainpage(request):
    #вывдо пагинации доступных презентаций и событий
    #events = get_pagination_events(request, request.GET.get('evp'),10)
    #broadcastings = get_pagination_broadcastings(request, request.GET.get('brp'),10)
    broadcastings = Broadcasting.objects.all()
    html = render_to_response('search.html', {'broadcastings':broadcastings }, context_instance=RequestContext(request))
    return HttpResponse(html)
    
#список доступных пользователю каналов
def event_list(request):
    events = get_pagination_events(request, request.GET.get('evpage'),10)
    html = render_to_response('event_list.html', {'events': events}, context_instance=RequestContext(request))
    return HttpResponse(html)

#список доступных пользователю каналов
def broadcasting_list(request):
    broadcastings = get_pagination_broadcastings(request, request.GET.get('brp'),10)
    html = render_to_response('broadcasting_list.html', {'broadcastings': broadcastings }, context_instance=RequestContext(request))
    return HttpResponse(html)

#презентация (слайды описание, доп даныне связанные с ней)
def broadcasting(request, id):
    try:
        broadcasting = Broadcasting.objects.get(pk=int(id))
    except Broadcasting.DoesNotExist:
        raise Http404
    slides = broadcasting.slides.all()
    html = render_to_response('broadcasting.html', {'broadcasting': broadcasting}, context_instance=RequestContext(request))
    return HttpResponse(html)

#канал (доступные презентации, описание канала)
#для владельца возможность редактирования данных
def event(request, id):
    event = Event.objects.get(pk=id)
    html = render_to_response('event.html', {'event': event }, context_instance=RequestContext(request))
    return HttpResponse(html)
    
# redirect на канал пользователя channel(id)
def mycabinet(request):
    if not request.user.is_authenticated():
        return redirect('/')
