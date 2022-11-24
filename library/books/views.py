from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def list(request):
    books =  Book.objects.all()
    return render(request, "book-list.html", {"books": books})

@login_required
def show(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, "show.html", {"book": book})

def handle_404(request, exception):
    data = { 'err' : exception }
    return render(request, "404.html", data)

def handle_500(request):
    return render(request, "500.html")
