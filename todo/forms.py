from django import forms
from .models import todo


class todo_form(forms.Form):
    todo_item = forms.CharField(max_length=1200,widget=forms.Textarea(
            attrs={
                "rows":1,
                "columns":30,
            }
        ),
        label=""
    )