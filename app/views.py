from django.shortcuts import render
from app.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login')
        except:
            messages.error(request, 'Account creation failed')
            return redirect('/signup')
    else:
        return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('/')