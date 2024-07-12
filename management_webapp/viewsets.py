from rest_framework import viewsets
from management_webapp.models import CourseProgram, Tuition  # Use singular CourseProgram
from management_webapp.serializers import CourseProgramSerializer, TuitionSerializer  # Use the correct serializers


class CourseProgramViewSet(viewsets.ModelViewSet):  # Use singular CourseProgramViewSet
    queryset = CourseProgram.objects.all()
    serializer_class = CourseProgramSerializer


class TuitionViewSet(viewsets.ModelViewSet):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer  # Correct the serializer class
