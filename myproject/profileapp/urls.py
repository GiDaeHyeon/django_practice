from .views import ProfileCreateView, ProfileUpdateView
from django.urls import path

app_name="profileapp"

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('create/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]