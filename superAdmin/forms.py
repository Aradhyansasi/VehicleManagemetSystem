from django import forms
from  superAdmin.models import Details

class VehicleRegistrationForm(forms.ModelForm):
    class Meta:
        model=Details
        fields=[
            'vehicle_number',
            'vehicle_type',
            'vehicle_model',
            'vehicle_description',
        ]
