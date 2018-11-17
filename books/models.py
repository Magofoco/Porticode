import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from books.constants import EXCHANGE_CHOICES, CONDITION_CHOICES, STATUS_CHOICES, OPEN
from books.constants import GENDER_CHOICES, PREFERENCE_CHOICES


class Book(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    original_poster = models.ForeignKey(User, on_delete=models.CASCADE)
    book_price = models.FloatField(default=0)
    exchange_choices = models.CharField(max_length=100, choices=EXCHANGE_CHOICES)
    condition_choices = models.CharField(
        max_length=100,
        choices=CONDITION_CHOICES,
    )
    status_choices = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=OPEN,
    )

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d %B %Y')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    preference1 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True,
                                   default=PREFERENCE_CHOICES[0][0])
    preference2 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True,
                                   default=PREFERENCE_CHOICES[4][0])
    preference3 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True,
                                   default=PREFERENCE_CHOICES[3][0])
    preference4 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True,
                                   default=PREFERENCE_CHOICES[13][0])
    preference5 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True,
                                   default=PREFERENCE_CHOICES[5][0])
    birth_date = models.DateField(null=True, default=datetime.date(1995, 7, 12))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, default=GENDER_CHOICES[0][1])
    location = models.CharField(max_length=150, null=True, default="London, Fulham")



# we are hooking the create_user_profile and save_user_profile methods to the User model,
# whenever a save event occurs. This kind of signal is called post_save

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("a")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
