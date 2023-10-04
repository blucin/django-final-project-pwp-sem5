from django.shortcuts import render
from app.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .forms import SignupForm

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'isLogin': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else ''
    }
    return render(request, 'index.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')
    else:
        return render(request, 'login.html')

def signup_view(request):
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login')

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)
            

def logout_view(request):
    logout(request)
    return redirect('/')