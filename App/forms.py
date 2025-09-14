from django.forms import ModelForm
from App.models import registermodel

class UserForm(ModelForm):
    class Meta:
        model = registermodel
        field = ["name","email","phone","password","address","gender","role","profilepicture"]


