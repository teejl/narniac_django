from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login-page/', views.login_page, name='login-page'),
    path('main/', views.main, name='main'),
    path('singup/', views.signup, name='signup'),
]
