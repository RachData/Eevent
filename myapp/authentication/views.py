from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib.auth.backends import ModelBackend

def login_view(request):
    # ... (code for login_view)
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def signup(request):
    # ... (code for signup)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_organizer:
                user.is_organizer = True
                user.save()
            #login(request, user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    # ... (code for logout_view)
    logout(request)
    return redirect('login')