from django.http import HttpResponse
from django.shortcuts import render
from .models import Poll

def index(request):
    
    context = {'umfragen': Poll.objects.all(), 'titel': "Umfragenseite"}
    return render(request, "polls/index.html", context)

def umfrage_detail(request, slug):
    umfrage = Poll.objects.get(slug=slug)
    return HttpResponse('{0}'.format(umfrage.name))