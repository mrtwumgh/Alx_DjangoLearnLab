from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'books', views.BookViewSet, basename='book')

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
] + router.url