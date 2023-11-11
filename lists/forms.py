from django import forms
from django.forms import ModelForm, TextInput
from .models import *

# ModelForms


class ListNameForm(ModelForm):
    class Meta:
        model = ListName
        fields = ['list_name']
        labels = {"list_name": ""}
        widgets = {
            'list_name': TextInput(attrs={
                'class': 'newList',
            })
        }


class UpdateListForm(forms.Form):
    list_name = forms.CharField(max_length=100)


class ListItemForm(ModelForm):
    class Meta:
        model = ListItem
        fields = ['list_item']
        labels = {'list_item': ""}


class UpdateItemForm(forms.Form):
    list_item = forms.CharField(max_length=100)
