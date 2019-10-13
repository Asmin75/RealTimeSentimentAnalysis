from django import forms


class UserInput(forms.Form):
    Message = forms.CharField(required=True, max_length=500)