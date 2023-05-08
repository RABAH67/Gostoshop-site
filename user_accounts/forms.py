from django import forms
from django.contrib.auth.forms import AuthenticationForm ,UsernameField ,UserCreationForm 
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):

	username = UsernameField(label='Nom',widget=forms.TextInput(attrs={'autofocus':'True','class':'oo'}))
	password = forms.CharField(label='Mot De Passe',widget=forms.PasswordInput(attrs={'autofocus':'True','class':'oo'}))


class SingUpForm(UserCreationForm):

	username = forms.CharField(label='Nom',widget=forms.TextInput(attrs={'autofocus':'True','class':'oo'}))
	password1 = forms.CharField(label='Mot De Passe',widget=forms.PasswordInput(attrs={'autofocus':'True','class':'oo'}))
	password2 = forms.CharField(label='Confirme Mot De Passe',widget=forms.PasswordInput(attrs={'autofocus':'True','class':'oo'}))

	class Meta:
		model = User
		fields = ['username','password1','password2']


