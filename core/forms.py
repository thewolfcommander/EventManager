from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.models import *



class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'name', 'message')

class ReportForm(forms.ModelForm):
    class Meta:
        model = ProblemReport
        fields = ('email', 'name', 'message', 'problem_screenshot')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('email', 'name', 'message', 'rating')
