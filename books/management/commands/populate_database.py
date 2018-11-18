from books.constants import EXCHANGE_CHOICES, CONDITION_CHOICES, STATUS_CHOICES, OPEN
from books.constants import GENDER_CHOICES, PREFERENCE_CHOICES
import random
from django.core.management.base import BaseCommand
from books.models import Book, User
from utils.google_api import get_info_from_api
import datetime


class Command(BaseCommand):
    args = ''
    help = 'command for popualting database'

    def _create_users(self):
        names = ["Ollie", "Jesse", "Cole", "Jude", "Jacob", "Leighton", "Alistar", "Olliver", "Tom", "Mike", "Patrick"]
        surnames = ["Smith", "Jones", "Williams", "Rooney", "Cole", "Taylor", "Evans", "Thomas", "Jonson", "Roberts",
                    "Walker"]
        name = random.choice(names)
        surname = random.choice(surnames)
        username = name + "_" + surname + str(random.randint(10, 100))
        email = username + "@gmail.com"
        user = User.objects.create_user(username=username,
                                        first_name=name,
                                        last_name=surname,
                                        email=email,
                                        password="francesco")
        u = User.objects.get(username=username)
        print(f"Created user {u.username}")

    def _create_books(self):
        i = 0
        while i < 1:
            response, str_isbn = get_info_from_api(i)
            i = +1
            if not response:
                continue
            else:
                user = User.objects.order_by('?').first()
                isbn = str_isbn
                title = response['ISBN:' + str_isbn]['title']
                url = (response['ISBN:' + str_isbn]['url'])
                year = int(response['ISBN:' + str_isbn]['publish_date'])
                date_published = datetime.date(year, 7, 12)
                body = response['ISBN:' + str_isbn]['by_statement']
                image = response['ISBN:' + str_isbn]['cover']['large']
                Book.objects.create(original_poster=user,
                                    title=title,
                                    pub_date=date_published,
                                    body = body,
                                    url = url,
                                    # image = models.ImageField(upload_to='images/', null=True),
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

def handle(self, *args, **options):
    for i in range(25):
        self._create_users()
    print("Successfully populated database with users!")
