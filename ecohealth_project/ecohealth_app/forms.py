from django import forms
from .models import HealthData

class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ('patient_id', 'medication', 'dosage', 'date_prescribed', 'expiry_date')