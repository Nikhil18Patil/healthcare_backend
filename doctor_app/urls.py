from django.urls import path
from .views import (
    DoctorListCreateAPIView, DoctorDetailAPIView
)

urlpatterns = [
 
    # Doctor APIs
    path('doctors/', DoctorListCreateAPIView.as_view(), name='doctors-list'),
    path('doctors/<uuid:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),

  
]
