from .models import Profile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
        widgets = {
            "image": forms.FileInput(),
            "displayname":forms.TextInput(attrs={"placeholder":"Add your name"}),
            "info":forms.Textarea(attrs={"placeholder":"Add some info about yourself"}),
        }
        
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['email']