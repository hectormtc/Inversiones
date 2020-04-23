from django import forms

from .models import Cliente

class PostForm(forms.ModelForm):
    model = Cliente
    fields = ('nombre', 'apellido','phone')
