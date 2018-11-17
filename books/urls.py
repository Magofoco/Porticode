from django.urls import path, include
from . import views

urlpatterns = [
    path('welcome', views.welcome, name="welcome"),
    path('home', views.home, name="home"),
    path('createfreebook', views.createfreebook, name="createfreebook"),
    path('createexchangebook', views.createexchangebook, name="createexchangebook"),

    path("<int:book_id>", views.detail, name="detail"),
]
