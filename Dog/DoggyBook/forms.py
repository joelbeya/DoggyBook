
#-*- coding: utf-8 -*-
from django import forms

class ImageUploadForm_user(forms.Form):
    """Image upload form."""
    image = forms.ImageField()



class ImageUploadForm_chien(forms.Form):
    """Image upload form."""
    image = forms.ImageField()



class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
