from django.urls import path
from .views import (
    PatientDoctorMappingListCreateAPIView, PatientDoctorMappingDetailAPIView
)

urlpatterns = [

    # Patient-Doctor Mapping APIs
    path('mappings/', PatientDoctorMappingListCreateAPIView.as_view(), name='mappings-list'),
    path('mappings/<uuid:patient_id>/', PatientDoctorMappingDetailAPIView.as_view(), name='patient-mappings'),
    path('mappings/delete/<uuid:pk>/', PatientDoctorMappingDetailAPIView.as_view(), name='delete-mapping'),
]
