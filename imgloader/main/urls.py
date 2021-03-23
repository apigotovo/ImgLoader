from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import UserRegistration

urlpatterns = [
    # path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegistration.as_view(), name='registration'),
]
