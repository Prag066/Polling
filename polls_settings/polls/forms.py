from django import forms

from .models import Question,Choice
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']

class Log_inForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
