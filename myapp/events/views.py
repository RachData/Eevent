from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Event
from .forms import EventForm
from rest_framework import viewsets


@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def is_organizer(user):
    # ... (code for is_organizer)
	return user.is_organizer

@login_required
def home(request):
    # ... (code for home)
    if request.user.is_organizer:
        events = Event.objects.filter(user=request.user)
    else:
        events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

@login_required
@user_passes_test(is_organizer, login_url='login')
def create_event(request):
    # ... (code for create_event)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

@login_required
@user_passes_test(is_organizer, login_url='login')
def update_event(request, event_id):
    # ... (code for update_event)
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form})

@login_required
@user_passes_test(is_organizer, login_url='login')
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return redirect('home')