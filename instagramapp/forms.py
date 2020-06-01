from django import forms
from django.db import models
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class PostingForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = "POST"
    helper.add_input(Submit('User', 'User', css_class='btn-primary'))

    class Meta:
        model = User
        fields = [
            'image',
            'caption',
            'location'
        ]

