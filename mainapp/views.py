from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *
from django.contrib.postgres.search import TrigramSimilarity



# class CenterModelViewSet(viewsets.ModelViewSet):
#     queryset = Center.objects.all()
#     serializer_class = CentersSerializer


# class CoursesModelViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class=CoursesSerializer


class VacansiesAPI(APIView):
    def get(self, request):
        text = request.query_params.get("name")
        vacansies = Vacancy.objects.all()
        if text:
            vacansies = Vacancy.objects.annotate(
                similarity = TrigramSimilarity("name", text)
            ).filter(similarity__gt=0.6)
        serializer = VacansysSerializer(vacansies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(selVacancy,request):
        serializer = VacansysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CoursesAPIView(APIView):
    def get(self, request):
        text = request.query_params.get("name")
        courses = Course.objects.all()
        if text:
            courses = Course.objects.annotate(
                similarity = TrigramSimilarity("name", text)
            ).filter(similarity__gt=0.6)
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(selVacancy,request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CenterAPIView(APIView):
    def get(self, request):
        text = request.query_params.get("name")
        centers = Center.objects.all()
        if text:
            centers = Center.objects.annotate(
                similarity=TrigramSimilarity("name", text)
            ).filter(similarity__gt=0.6)
        serializer = CentersSerializer(centers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(selVacancy, request):
        serializer = CentersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
