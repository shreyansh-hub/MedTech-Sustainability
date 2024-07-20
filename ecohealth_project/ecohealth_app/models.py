from django.db import models

class HealthData(models.Model):
    patient_id = models.CharField(max_length=100)
    medication = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    date_prescribed = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.patient_id} - {self.medication}"