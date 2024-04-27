from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *



class CenterModelViewSet(viewsets.ModelViewSet):
    queryset = Center.objects.all()
    serializer_class = CentersSerializer


class CoursesModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class=CoursesSerializer


class VacansysModelViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacansysSerializer

