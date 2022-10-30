from django.forms import ModelForm

from users.models import UserQuery

class UserForm(ModelForm):
    class Meta:
        model = UserQuery
        fields = ['userID', 'messageBody']