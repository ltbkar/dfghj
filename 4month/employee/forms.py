from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    experience = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.CustomEmployee
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'age',
                  'phone_number',
                  'experience',
                  'gender')

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomEmployee)
def set_category(sender, instance, created, **kwargs):
    if created:
        print('The signal has been processed, the employee has been created')
        experience = instance.age
        if experience < 2:
            instance.category = "Junior"
        elif 2 <= experience <= 4:
            instance.category = "Strong Junior"
        elif 4 <= experience <= 8:
            instance.category = "Middle"
        elif 8 <= experience <= 12:
            instance.category = "Strong Middle"
        elif 12 <= experience <= 18:
            instance.category = "Senior"
        elif 18 <= experience <= 30:
            instance.category = "Strong Senior"
        else:
            instance.category = "Category is not Defined"
        instance.save()
