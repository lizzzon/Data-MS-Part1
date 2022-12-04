from django.urls import path

from apps.base.views import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
]
