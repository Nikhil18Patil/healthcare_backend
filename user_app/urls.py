from django.urls import path
from .views import (
    RegisterUserAPIView, LoginAPIView
)

#the url endpoints below is according to given assignment
urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login')
]
