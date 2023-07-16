from django import forms
from .models import *

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш Email', max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = ContactUsModel
        fields = ['name', 'email', 'message', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-controlt'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

