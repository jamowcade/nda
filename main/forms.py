from django import forms
from .models import ScanCase

class ScanCaseForm(forms.ModelForm):
    class Meta:
        model = ScanCase
        fields = ['scan_date', 'name', 'description']
        widgets = {
            'scan_date': forms.DateInput(attrs={'type': 'date'}),
        }