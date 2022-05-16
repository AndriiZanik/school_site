from django import forms
from contact.models import Responses


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ['name','email','response']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'response':forms.Textarea(attrs={"class": "form-control",'rows': 6}),
        }
