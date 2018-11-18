from books.constants import EXCHANGE_CHOICES, CONDITION_CHOICES, STATUS_CHOICES, OPEN
from django.core.files import File
from books.constants import GENDER_CHOICES, PREFERENCE_CHOICES
from django.core.management.base import BaseCommand
from books.models import Book, User
from utils.google_api import get_info_from_api
import random
import urllib
import datetime
import string


def random_generator(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


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
        books_added = 0
        for int_isbn in [9780140361216, 9780545010221, 9780590353427, 9780060809836, 9781894063012, 9780156027496,
                         9780373626045, 5040071159, 9780141183190, 9780099285663, 9780028600901, 9780618832934,
                         9780618832934, 9781101084571, 9781101099421, 9781101096451, 9780439800990, 9780141439686,
                         9780969522508, 9780669281149, 9780495793595, 9780199540280, 9780618832934, 9780486475677]:
            response, str_isbn = get_info_from_api(int_isbn)
            if not response:
                print("No book with this ISBN")
                continue
            else:
                books_added += 1
                user = User.objects.order_by('?').first()
                title = response['ISBN:' + str_isbn]['title']
                url = (response['ISBN:' + str_isbn]['url'])
                # year = int(response['ISBN:' + str_isbn]['publish_date'][-4:])
                year = random.choice(range(1950, 2015))
                date_published = datetime.date(year, 7, 12)
                if 'by_statement' in response['ISBN:' + str_isbn].keys():
                    body = response['ISBN:' + str_isbn]['by_statement']
                if 'cover' in response['ISBN:' + str_isbn].keys():
                    image_link = response['ISBN:' + str_isbn]['cover']['large']
                    if image_link[-3:] != 'jpg':
                        continue
                    filename = random_generator() + ".jpg"
                    urllib.request.urlretrieve(image_link, filename)
                print(title)
                condition = random.choice([x[1] for x in CONDITION_CHOICES])
                exchange = random.choice([x[1] for x in EXCHANGE_CHOICES])
                status = random.choice([x[1] for x in EXCHANGE_CHOICES])
                book = Book(original_poster=user,
                            title=title,
                            pub_date=date_published,
                            body=body,
                            url=url,
                            exchange_choices=exchange,
                            condition_choices=condition,
                            status_choices=status)
                book.image = File(open(filename, 'rb'))
                book.save()
        print(f"Successfully populated database with {books_added} new books!")

    def handle(self, *args, **options):
        # for i in range(25):
        #     self._create_users()
        # print("Successfully populated database with users!")

        self._create_books()
