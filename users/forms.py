from sqlite3 import Timestamp
from django.forms import ModelForm
from django import forms

from users.models import UserQuery

class UserForm(ModelForm):
    # userID = forms.NumberInput()
    # messageBody = forms.TextInput()

    class Meta:
        model = UserQuery
        fields = '__all__'