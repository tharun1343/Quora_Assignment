from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2","first_name","last_name")

    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class Add_Question(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']

class Add_answer(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['answer']