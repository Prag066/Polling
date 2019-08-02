from django import forms

from .models import Question,Choice,Profile
from django.contrib.auth.models import User
from django.core.validators import validate_email

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class Log_inForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    confirm_password= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            ma=validate_email(email)
        except:
            raise forms.ValidationError("email not correct")
        return email

    def clean_confirm_password(self):
        p = self.cleaned_data['password']
        cp = self.cleaned_data['confirm_password']
        if (p!=cp):
            raise forms.ValidationError("password are not matched,")
