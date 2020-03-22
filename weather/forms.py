from django.forms import ModelForm, TextInput
from .models import Cidade


class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Nome da Cidade'})}