from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class CustomEmployee(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    phone_number = models.CharField(max_length=14, default="+996")
    age = models.IntegerField(default=18, validators=[MinValueValidator(18), MaxValueValidator(99)])
    experience = models.PositiveIntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(30)], max_length=30)
    gender = models.CharField(max_length=100, choices=GENDER)
    category = models.CharField(max_length=100, default="category is not Detected")
    description = models.TextField(verbose_name='Write the small description of your experience')
    recommendation = models.CharField(verbose_name="Which companies did you worked in the past and describe the "
                                                   "reasons why did you prefer our company",
                                      blank=True, max_length=100)
    job = models.CharField(verbose_name="What position are you applying for?", max_length=50)
    salary = models.PositiveIntegerField(verbose_name="how much money do you want per month for your work?",
                                         default=2500)
    preferences = models.CharField(verbose_name="Did you feel comfortable to work with the colleague from other "
                                                "countries and genders?",
                                   default='Yes', max_length=100)
    duration = models.PositiveIntegerField(verbose_name="How long are you going to work in our company?",
                                           default=10)


@receiver(post_save, sender=CustomEmployee)
def set_category(sender, instance, created, **kwargs):
    if created:
        print('The signal has been processed, the employee has been created')
        experience = instance.experience
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

