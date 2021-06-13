from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, hello_world

app_name="accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),

    path('login/', LoginView.as_view(template_name=f'{app_name}/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]