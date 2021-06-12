from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import AccountCreateView, hello_world

app_name="accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),

    path('login/', LoginView.as_view(template_name=f'{app_name}/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
]