from rest_framework import viewsets
from .models import CourseProgram, StudentProfile, LecturerProfile
from .serializers import CourseProgramSerializer, StudentProfileSerializer, LecturerProfileSerializer


class CourseProgramViewSet(viewsets.ModelViewSet):
    queryset = CourseProgram.objects.all()
    serializer_class = CourseProgramSerializer

    def list(self, request, *args, **kwargs):
        print("List CoursePrograms endpoint hit")
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print("Retrieve CourseProgram endpoint hit")
        return super().retrieve(request, *args, **kwargs)


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class LecturerProfileViewSet(viewsets.ModelViewSet):
    queryset = LecturerProfile.objects.all()
    serializer_class = LecturerProfileSerializer
