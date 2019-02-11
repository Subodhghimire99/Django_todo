from django import forms

from .models import todo

class addtodo_form(forms.Form):
	todo_item = forms.CharField()