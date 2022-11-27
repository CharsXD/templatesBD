from django import forms
from templatesApp.models import User

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
