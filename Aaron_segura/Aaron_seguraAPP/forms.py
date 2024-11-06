from django import forms 
from Aaron_seguraAPP.models import Django_Seminario

class FormSeminario(forms.ModelForm):
    class Meta:
        model = Django_Seminario
        fields = '__all__'