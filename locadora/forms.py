from django.forms import ModelForm
from django import forms
from .models import Filme

class FilmeForm(ModelForm):

    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control' }),
            'genero' : forms.TextInput(attrs={'class': 'form-control' }),
            'duracao' : forms.NumberInput(attrs={'class': 'form-control' }),
            'ano_lancamento' : forms.NumberInput(attrs={'class': 'form-control' }),
            'sinopse' : forms.Textarea(attrs={'class': 'form-control' }),
            'imagem' : forms.FileInput(attrs={'class': 'form-control'}),
        }