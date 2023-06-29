from django import forms
from .models import *
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import List
from blog import models
class PostForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new blog'}))
    description=forms.Textarea()

    class Meta:
        model = Post
        fields=('title','description')
class ListForm(forms.ModelForm):
    class Meta:
        model=List
        fields=["item","completed"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','email','password1','password2']