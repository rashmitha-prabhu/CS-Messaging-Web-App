from sqlite3 import Timestamp
from django.forms import ModelForm
from django import forms

from users.models import UserQuery

class UserForm(ModelForm):
    class Meta:
        model = UserQuery
        fields = ['userID', 'messageBody']