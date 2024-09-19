from django.urls import path, include
from accounts import views as accounts_views
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'profile', accounts_views.ProfileModelView, basename='profile')

urlpatterns = [
    path('register/', accounts_views.RegisterAPIViewset.as_view(), name='register'),
    path('login/', accounts_views.LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]