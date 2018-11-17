from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    original_poster = models.ForeignKey(User, on_delete=models.CASCADE)
    book_price = models.FloatField(default=0)


    FREE="FR"
    PAID="PA"
    BARTER="BA"

    EXCHANGE_CHOICES = (
        (FREE, 'Free'),
        (PAID, 'Paid'),
        (BARTER, 'Barter')
    )
    exchange_choices = models.CharField(max_length=100, choices=EXCHANGE_CHOICES)


    NEW='NE'
    USED_NEW='UN'
    USED_GOOD='UG'
    USED_JADED='UJ'
    CONDITION_CHOICES = (
        (NEW, 'New - Never Used'),
        (USED_NEW, 'Used but seems still new'),
        (USED_GOOD, 'Used but in good conditions'),
        (USED_JADED, 'Used and you can see it')
    )

    condition_choices = models.CharField(
        max_length=100,
        choices=CONDITION_CHOICES,
    )


    OPEN='OP'
    PENDING='PE'
    EXCHANGED='EX'

    STATUS_CHOICES = (
        (OPEN, 'Open to trade'),
        (PENDING, 'Pending for approval'),
        (EXCHANGED, 'Exhanged already')
    )

    status_choices = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=OPEN,
    )


    def pub_date_pretty(self):
      return self.pub_date.strftime('%d %B %Y')
