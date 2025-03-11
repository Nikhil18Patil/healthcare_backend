import uuid
from django.db import models
from doctor_app.models import Doctor
from patient_app.models import Patient

class PatientDoctorMapping(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="assigned_doctors")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patients")
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['patient', 'doctor']

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
