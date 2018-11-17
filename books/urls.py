from django.urls import path, include
from . import views

urlpatterns = [
    path('welcome', views.welcome, name="welcome"),
    path('allbooks', views.allbooks, name="allbooks"),
    path('freebooks', views.freebooks, name="freebooks"),
    path('exchangebooks', views.exchangebooks, name="exchangebooks"),
    path('createfreebook', views.createfreebook, name="createfreebook"),
    path('createexchangebook', views.createexchangebook, name="createexchangebook"),
    path("<int:book_id>", views.detail, name="detail"),
]
