from django.test import Client, TestCase
from django.urls import reverse

from .models import Author, Book

class BaseTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_author = Author.objects.create(name='Rick Riordan')
        cls.book = Book.objects.create(name='Percy Jackson', author=cls.test_author)

class TestBasicViews(BaseTestCase):
    client = Client()

    def test_home(self):
        response = self.client.get(reverse('books-home'))
        assert "home.html" in [t.name for t in response.templates]

    def test_about(self):
        response = self.client.get(reverse('books-about'))
        assert "about.html" in [t.name for t in response.templates]

    def test_list(self):
        response = self.client.get(reverse('books-list'))
        assert "books" in response.context
        assert response.context['books'].count() == 1
        assert "book-list.html" in [t.name for t in response.templates]

    # def test_show(self):
    #     response = self.client.get(reverse('books-show', args=[1]))
    #     # print(response.context)
    #     assert "book" in response.context
    #     assert response.context['book'].name == 'Percy Jackson'
    #     assert response.context['book'].author.name == 'Rick Riordan'
    #     assert "show.html" in [t.name for t in response.templates]
