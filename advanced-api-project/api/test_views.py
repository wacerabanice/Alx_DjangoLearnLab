from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Create test user
        self.user = User.objects.create_user(
            username="testuser", password="pass123"
        )

        # Authentication token (if you use TokenAuth)
        self.client.login(username="testuser", password="pass123")

        # Sample books
        self.book1 = Book.objects.create(
            title="Django Basics",
            author="John Doe",
            published_year=2020
        )
        self.book2 = Book.objects.create(
            title="Advanced API Design",
            author="Jane Doe",
            published_year=2023
        )

        self.list_url = reverse("books-list")
        self.create_url = reverse("books-create")


    # -------------------------
    # 📌 TEST CREATE
    # -------------------------
    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Author X",
            "published_year": 2024
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")


    # -------------------------
    # 📌 TEST LIST
    # -------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 2)


    # -------------------------
    # 📌 TEST UPDATE
    # -------------------------
    def test_update_book(self):
        url = reverse("books-update", args=[self.book1.id])
        data = {"title": "Updated Title"}

        response = self.client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")


    # -------------------------
    # 📌 TEST DELETE
    # -------------------------
    def test_delete_book(self):
        url = reverse("books-delete", args=[self.book1.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())


    # -------------------------
    # 📌 TEST SEARCH
    # -------------------------
    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Django"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Django" in b["title"] for b in response.data))


    # -------------------------
    # 📌 TEST FILTER
    # -------------------------
    def test_filter_books_by_year(self):
        response = self.client.get(self.list_url, {"published_year": 2023})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["published_year"], 2023)


    # -------------------------
    # 📌 TEST ORDERING
    # -------------------------
    def test_order_books_by_year(self):
        response = self.client.get(self.list_url, {"ordering": "-published_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]["published_year"] >= response.data[1]["published_year"])
