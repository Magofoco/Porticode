from django.db import models
from django.contrib.auth.models import User
from books.constants import EXCHANGE_CHOICES, CONDITION_CHOICES, STATUS_CHOICES, OPEN
from books.constants import GENRE_CHOICES, PREFERENCE_CHOICES


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    college = models.CharField(max_length=30)
    preference1 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True)
    preference2 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True)
    preference3 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True)
    preference4 = models.CharField(max_length=100, choices=PREFERENCE_CHOICES, null=True)
    birth_date = models.DateField(null=True)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, null=True)
    location = models.CharField(max_length=150, null=True)
