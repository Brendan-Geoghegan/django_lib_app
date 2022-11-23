from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def list(request):
    books =  Book.objects.all()
    return render(request, "book-list.html", {"books": books})

def show(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, "show.html", {"book": book})

def handle_404(request, exception):
    return render(request, "404.html")
