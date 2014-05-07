from django.db import models

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator



class UserProfile(models.Model):
    def __str__(self):
        return self.studentid

    user = models.ForeignKey(User)
    name = models.CharField(max_length=5)
    studentid = models.CharField(max_length=10,)
                                #validators=[MinLengthValidator(10)])
    cellphone = models.CharField(max_length=11)

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields=('name','studentid','cellphone')

class UserForm(UserCreationForm):
    pass

class GroupProfile(models.Model):
    def __str__(self):
        return self.name1

    user=models.ForeignKey(User)

    name1 = models.CharField(max_length=5)
    studentid1 = models.CharField(max_length=10)
    phone1 = models.CharField(max_length=11)

    name2 = models.CharField(max_length=5)
    studentid2 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=11)

class GroupForm(ModelForm):

    class Meta:
        model = GroupProfile
        fields=('name1','studentid1','phone1','name2','studentid2','phone2')
