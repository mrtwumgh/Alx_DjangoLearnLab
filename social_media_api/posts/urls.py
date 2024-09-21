from rest_framework import routers
from posts import views as posts_views
from django.urls import path, include



router = routers.DefaultRouter()
router.register(r'posts', posts_views.PostViewSet, basename='post')
router.register(r'comments', posts_views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
