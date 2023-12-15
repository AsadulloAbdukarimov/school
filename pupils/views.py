from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from . models import Exam_materials, Courses, BestPupils
from . serializers import Exam_materialsSerializers,CoursesSerializers, BestPupilsSerializers


class Exam_materialsViewSet(ModelViewSet):
    serializer_class = Exam_materialsSerializers
    queryset = Exam_materials.objects.all()


class CoursesViewSet(ModelViewSet):
    serializer_class = CoursesSerializers
    queryset = Courses.objects.all()


class BestPupilsViewSet(ModelViewSet):
    serializer_class = BestPupilsSerializers
    queryset = BestPupils.objects.all()

