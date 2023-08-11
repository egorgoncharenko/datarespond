from django import forms
from .models import Respondent

class RespondentForm(forms.ModelForm):
    class Meta:
        model = Respondent
        fields = ['okpo', 'full_name', 'okved', 'inn', 'number', 'email']
