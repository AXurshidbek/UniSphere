from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *




urlpatterns = [
    path('/courses',CoursesAPIView.as_view()),
    path('/centers',CoursesAPIView.as_view()),
    path('/vacansies',CoursesAPIView.as_view())
]