from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import StudentProfile, LecturerProfile
from .serializers import UserSerializer, StudentProfileSerializer, LecturerProfileSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        profile_type = self.request.data.get('profile_type')
        profile_data = self.request.data

        if profile_type == 'student':
            student_serializer = StudentProfileSerializer(data={
                'user': user.id,
                'name': profile_data.get('name'),
                'email': profile_data.get('email'),
                'phone': profile_data.get('phone'),
                'address': profile_data.get('address'),
                'marks': profile_data.get('marks', 0),
            })
            if student_serializer.is_valid():
                student_serializer.save(user=user)
            else:
                user.delete()
                raise serializers.ValidationError(student_serializer.errors)
        elif profile_type == 'lecturer':
            lecturer_serializer = LecturerProfileSerializer(data={
                'user': user.id,
                'name': profile_data.get('name'),
                'email': profile_data.get('email'),
                'phone': profile_data.get('phone'),
                'address': profile_data.get('address'),
                'program': profile_data.get('program')
            })
            if lecturer_serializer.is_valid():
                lecturer_serializer.save(user=user)
            else:
                user.delete()
                raise serializers.ValidationError(lecturer_serializer.errors)
        else:
            user.delete()
            raise serializers.ValidationError("Invalid profile type")
