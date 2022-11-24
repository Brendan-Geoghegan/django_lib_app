from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="books-home"),
    path("about/", views.about, name="books-about"),
    path("list/", views.list, name="books-list"),
    path("<int:id>/", views.show, name="books-show")
]


