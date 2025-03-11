from django.urls import path
from .views import (
    PatientListCreateAPIView, PatientDetailAPIView
)

urlpatterns = [
    # Patient APIs
    path('patients/', PatientListCreateAPIView.as_view(), name='patients-list'),
    path('patients/<uuid:pk>/', PatientDetailAPIView.as_view(), name='patient-detail')
    
]
