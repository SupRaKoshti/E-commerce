from django.forms import ModelForm
from App.models import registermodel

# class registermodel(models.Model):
#     name=models.CharField(max_length=20)
#     email=models.EmailField()
#     phone=models.CharField(max_length=15, unique=True)
#     password=models.CharField(max_length=100)
#     address=models.TextField()
#     gender=models.CharField(max_length=20)
#     role=models.CharField(max_length=20)
#     profilepicture=models.ImageField(upload_to='photos')
#
#     def profile_photo(self):
#         return mark_safe('<img src="{}" width="100"/>'.format(self.profilepicture.url))
#
#     profile_photo.allow_tags = True
#
#     def __str__(self):
#         return self.name

class UserForm(ModelForm):
    class Meta:
        model = registermodel
        field = ["name","email","phone","password","address","gender","role","profilepicture"]


