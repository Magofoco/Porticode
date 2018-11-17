from django.urls import path, include
from . import views

urlpatterns = [
    path('welcome', views.welcome, name="welcome"),
    path('allbooks', views.allbooks, name="allbooks"),
    path('freebooks', views.freebooks, name="freebooks"),
    path('freebook/<int:book_id>', views.free_detail, name="freebook_detail"),
    path('exchangebooks', views.exchangebooks, name="exchangebooks"),
    path('exchangebook/<int:book_id>', views.exchangebook_detail, name="exchangebook_detail"),
    path('createfreebook', views.createfreebook, name="createfreebook"),
    path('createexchangebook', views.createexchangebook, name="createexchangebook"),
    path("<int:book_id>", views.detail, name="detail"),
    path("free_book_contact/<int:book_id>", views.free_book_contact, name="free_book_contact"),
]
