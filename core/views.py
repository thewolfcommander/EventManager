import random

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from .forms import *
from .models import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)



def about(request):
    context = {}
    return render(request, 'about.html', context)



def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = ReportForm()
    context = {'form': form}
    return render(request, 'report.html', context)


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    context = {'form': form}
    return render(request, 'feedback.html', context)

@login_required
def book_now_event(request, pk=None, *args, **kwargs):
    qs = Event.objects.all()
    if request.method == 'POST':
        form = BookEventForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.events = Event.objects.get(pk=pk)
            form.save()
            return redirect('event')
    else:
        form = BookEventForm()
    try:
        object_1 = random.randint(0, len(qs)-1)
        object_2 = random.randint(0, len(qs)-1)
        object_3 = random.randint(0, len(qs)-1)
        if object_1 == object_2:
            object_1 = random.randint(0, len(qs)-1)
        elif object_1 == object_3:
            object_1 = random.randint(0, len(qs)-1)
        else:
            object_2 = random.randint(0, len(qs)-1)
        obj = Event.objects.get(pk=pk)
        event_1 = qs[object_1]
        event_2 = qs[object_2]
        event_3 = qs[object_3]
        context = {
            'obj': obj,
            'form': form,
            'event_1': event_1,
            'event_2': event_2,
            'event_3': event_3,
        }
        return render(request, 'book_now_event.html', context)
    except IndexError:
        print("Index out of Range")
        context = {
            'obj': obj,
        }
        return render(request, 'book_now_event.html', context)

@login_required
def book_now_location(request, pk=None, *args, **kwargs):
    qs = Location.objects.all()
    if request.method == 'POST':
        form = BookLocationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.events = Location.objects.get(pk=pk)
            form.save()
            return redirect('location')
    else:
        form = BookLocationForm()
    try:
        object_1 = random.randint(0, len(qs)-1)
        object_2 = random.randint(0, len(qs)-1)
        object_3 = random.randint(0, len(qs)-1)
        if object_1 == object_2:
            object_1 = random.randint(0, len(qs)-1)
        elif object_1 == object_3:
            object_1 = random.randint(0, len(qs)-1)
        else:
            object_2 = random.randint(0, len(qs)-1)
        obj = Location.objects.get(pk=pk)
        event_1 = qs[object_1]
        event_2 = qs[object_2]
        event_3 = qs[object_3]
        context = {
            'obj': obj,
            'form': form,
            'event_1': event_1,
            'event_2': event_2,
            'event_3': event_3,
        }
        return render(request, 'book_now.html', context)
    except IndexError:
        print("Index out of Range")
        context = {
            'obj': obj,
        }
        return render(request, 'book_now.html', context)


@login_required
def event(request):
    events = Event.objects.all().order_by('-updated_date')
    context = {
        'events': events,
    }
    return render(request, 'event.html', context)

@login_required
def event_detail(request, pk=None, *args, **kwargs):
    qs = list(Event.objects.all())
    try:
        object_1 = random.randint(0, len(qs)-1)
        object_2 = random.randint(0, len(qs)-1)
        object_3 = random.randint(0, len(qs)-1)
        if object_1 == object_2:
            object_1 = random.randint(0, len(qs)-1)
        elif object_1 == object_3:
            object_1 = random.randint(0, len(qs)-1)
        else:
            object_2 = random.randint(0, len(qs)-1)
        event_1 = qs[object_1]
        event_2 = qs[object_2]
        event_3 = qs[object_3]
        obj = Event.objects.get(pk=pk)
        context = {
            'qs': qs,
            'obj': obj,
            'event_1': event_1,
            'event_2': event_2,
            'event_3': event_3,
        }
        return render(request, 'event_detail.html', context)
    except IndexError:
        print("Index out of Range")
        context = {
            'obj': obj,
        }
        return render(request, 'event_detail.html', context)


@login_required
def location(request):
    locations = Location.objects.all().order_by('-updated_date')
    context = {
        'locations': locations,
    }
    return render(request, 'location.html', context)

@login_required
def location_detail(request, pk=None, *args, **kwargs):
    qs = list(Location.objects.all())
    try:
        object_1 = random.randint(0, len(qs)-1)
        object_2 = random.randint(0, len(qs)-1)
        object_3 = random.randint(0, len(qs)-1)
        if object_1 == object_2:
            object_1 = random.randint(0, len(qs)-1)
        elif object_1 == object_3:
            object_1 = random.randint(0, len(qs)-1)
        else:
            object_2 = random.randint(0, len(qs)-1)
        location_1 = qs[object_1]
        location_2 = qs[object_2]
        location_3 = qs[object_3]
        obj = Location.objects.get(pk=pk)
        context = {
            'qs': qs,
            'obj': obj,
            'location_1': location_1,
            'location_2': location_2,
            'location_3': location_3,
        }
        return render(request, 'location_detail.html', context)
    except IndexError:
        print("Index out of Range")
        context = {
            'obj': obj,
        }
        return render(request, 'location_detail.html', context)

@login_required
def settings(request):
    context = {}
    return render(request, 'settings.html', context)


def page404(request):
    context = {}
    return render(request, '404.html', context)


def page500(request):
    context = {}
    return render(request, '500.html', context)

