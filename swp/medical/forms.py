from django import forms
from .models import MedicalLeave

class MedicalLeaveForm(forms.ModelForm):
    class Meta:
        model=MedicalLeave
        fields=(
        'leave_from','leave_to','hometown','reason'
        )
