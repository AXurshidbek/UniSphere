from rest_framework import serializers
from .models import *


class CentersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Center
        fields='__all__'

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class VacansysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vacancy
        fields='__all__'

class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pictures
        fields='__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

