from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Choice, Poll

def index(request):
    
    context = {'umfragen': Poll.objects.all(), 'titel': "Umfragenseite"}
    return render(request, 'polls/index.html', context)

def umfrage_detail(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage}
    return render(request=request, template_name='polls/umfrage.html', context=context)

def results(request, slug):     
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage}
    return render(request=request, template_name='polls/results.html', context=context)

def vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        ausgewaehlte_antwort = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("Fehler: Es wurde keine bzw. eine ungültige Antwort ausgewählt")
    else:
         ausgewaehlte_antwort.votes +=1
         ausgewaehlte_antwort.save()
         return HttpResponseRedirect(reverse('results', args=(umfrage.slug,)))

