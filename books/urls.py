from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path("<int:book_id>", views.detail, name="detail"),
]
