from django.shortcuts import render
from app.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import SignupForm, LoginForm, createPostForm, updatePostForm

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'isLogin': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else '',
        'form': createPostForm(request),
    }

    if request.method == 'POST':
        form = createPostForm(request)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            post = Post(title=title, content=content, author=request.user)
            post.save()
            return redirect('/')
        else:
            context['form'] = form

    return render(request, 'index.html', context)

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = updatePostForm(request, post)

    # check if the user is the author of the post
    if post.author != request.user:
        return redirect('/', messages.error(request, 'You are not the author of this post'))

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {
                'form': form,
                'post': post
            }
            return render(request, 'update_post.html', context)
    else:
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'update_post.html', context)
    
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    # check if the user is the author of the post
    if post.author != request.user:
        return redirect('/', messages.error(request, 'You are not the author of this post'))

    post.delete()
    return redirect('/')


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'login.html', context)

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

