from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from django.utils import timezone
from books.constants import BARTER, FREE, PAID


# Create your views here.

def welcome(request):
    return render(request, "books/welcome.html")


def allbooks(request):
    books = Book.objects
    return render(request, "books/allbooks.html", {"books": books})


def freebooks(request):
    books = Book.objects.filter(exchange_choices="FREE")
    return render(request, "books/freebooks.html", {"books": books})


def exchangebooks(request):
    books = Book.objects.filter(exchange_choices="BARTER")
    return render(request, "books/exchangebooks.html", {"books": books})


@login_required
def createfreebook(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.POST[
            'exchange_choices'] and request.POST['condition_choices']:
            book = Book()
            book.title = request.POST['title']
            book.body = request.POST['body']
            book.image = request.FILES['image']
            book.exchange_choices = request.POST['exchange_choices']
            book.condition_choices = request.POST['condition_choices']
            book.pub_date = timezone.datetime.now()
            book.original_poster = request.user
            book.save()
            return redirect('/books/' + str(book.id))
        else:
            return render(request, 'books/createfreebook.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'books/createfreebook.html')


@login_required
def createexchangebook(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.POST[
            'exchange_choices'] and request.POST['condition_choices']:
            book = Book()
            book.title = request.POST['title']
            book.body = request.POST['body']
            book.image = request.FILES['image']
            book.exchange_choices = request.POST['exchange_choices']
            book.condition_choices = request.POST['condition_choices']
            book.pub_date = timezone.datetime.now()
            book.original_poster = request.user
            book.save()
            return redirect('/books/' + str(book.id))
        else:
            return render(request, 'books/createexchangebook.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'books/createexchangebook.html')


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/detail.html", {"book": book})


def exchangebook_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/exchangebook_detail.html", {"book": book})


def free_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/free_detail.html", {"book": book})


def free_book_contact(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/free_book_contact.html")
