from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from app.models import Post

class SignupForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

def createPostForm(request):
    class CreatePostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'content']
    return CreatePostForm(request.POST or None)

def updatePostForm(request, post):
    class UpdatePostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'content']
    return UpdatePostForm(request.POST or None, instance=post)
