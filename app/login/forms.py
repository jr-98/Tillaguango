from django import forms

class formularioLogin(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput()) 