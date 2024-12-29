from django.urls import path
from .views import LoginView, HelloWorldView

urlpatterns = [
    path('login/', LoginView.as_view(), name='knox_login'),
    path('hello/', HelloWorldView.as_view(), name='hello_world')
]

