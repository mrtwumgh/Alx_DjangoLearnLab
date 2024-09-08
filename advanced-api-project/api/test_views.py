from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()

        self.book = Book.objects.create(
            title="Angels & Demons",
            author="Dan Brown",
            description="Test description",
            published_e="2023"
        )

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Unauthorized Book",
            "author": "Unauthorized Author",
            "description": "Unauthorized description",
            "published_date": "2023-09-02"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse('book-update', args=[self.book.id])
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "description": "Updated description",
            "published_date": "2023-09-03"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)