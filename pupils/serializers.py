from rest_framework.serializers import ModelSerializer

from .models import Exam_materials, Courses, BestPupils

class Exam_materialsSerializers(ModelSerializer):
    class Meta:
        model=Exam_materials
        fields='__all__'


class CoursesSerializers(ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'


class BestPupilsSerializers(ModelSerializer):
    class Meta:
        model=BestPupils
        fields='__all__'
