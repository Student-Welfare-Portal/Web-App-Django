from django import forms
from .models import MedicalLeave

class MedicalLeaveForm(forms.ModelForm):
    leave_from=forms.DateField(label='leave_from',widget=forms.TextInput(attrs={"class":"form-control"}))
    leave_to=forms.DateField(label='leave_to',widget=forms.TextInput(attrs={"class":"form-control"}))
    hometown=forms.CharField(label='hometown',widget=forms.TextInput(attrs={"class":"form-control"}))
    reason=forms.CharField(label='reason',widget=forms.Textarea(attrs={"class":"form-control","rows":"4","cols":"50"}))
    class Meta:
        model = MedicalLeave
        fields = ['leave_from','leave_to','hometown','reason']
