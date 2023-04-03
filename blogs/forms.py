from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blogs_Items



INPUT_CLASSES = "w-full py-4 px-6 rounded-2xl border"



class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs_Items
        fields = ('name', 'description', 'image')
        name = forms.CharField()
        description = forms.Textarea()
        image = forms.FileInput()