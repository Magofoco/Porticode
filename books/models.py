from django.db import models
from django.contrib.auth.models import User
from books.constants import EXCHANGE_CHOICES, CONDITION_CHOICES, STATUS_CHOICES, OPEN


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
