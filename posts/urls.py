from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PostListCreateview,
    PostRetrieveUpdateDestroyView,
    UserRegistrationView
)

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('token/',TokenObtainPairView.as_view(), name='token-pain-obtain'),
    path('token/refresh/',UserRegistrationView.as_view(), name='register'),
    path('posts/',PostListCreateview.as_view(), name='post-list-create'),
    path('posts/<int:pk>/',PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
]
