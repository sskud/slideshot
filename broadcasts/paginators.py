from broadcasts.models import Event, Broadcasting, Slide
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_pagination_events(request, page, count):
    if not request.user.is_authenticated():
        events_list = Event.objects.filter(is_public=True)
    else:
        events_list = Event.objects.filter(Q(members=request.user)|Q(members=request.user))
    paginator = Paginator(events_list, count) # Show 10 contacts per page
    
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)
    return events

def get_pagination_broadcastings(request, page, count):
    if not request.user.is_authenticated():
        br_list = Broadcasting.objects.filter(public=True)
    else:
        br_list = Broadcasting.objects.filter(Q(public=True)|Q(event__members=request.user)|Q(event__owner=request.user))
    paginator = Paginator(br_list, count) # Show 25 contacts per page
    try:
        br = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        br = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        br = paginator.page(paginator.num_pages)
    return br