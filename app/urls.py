from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('update_post/<int:pk>/', views.updatePost, name='update_post'),
    path('delete_post/<int:pk>/', views.deletePost, name='delete_post'),
]