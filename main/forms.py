from django import forms
from django.forms import ModelForm
from .models import Request_a_Demo

class RequestDemoForm(ModelForm):
    class Meta:
        model = Request_a_Demo
        fields = '__all__'  # Include all fields from the model
