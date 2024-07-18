from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CourseProgram, StudentProfile, LecturerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

class CourseProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgram
        fields = ['id', 'name', 'description', 'duration', 'tuition_fee']

class StudentProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    courses = serializers.PrimaryKeyRelatedField(queryset=CourseProgram.objects.all(), many=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'name', 'email', 'phone', 'courses', 'marks', 'address', 'created_at', 'updated_at']

class LecturerProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    program = serializers.PrimaryKeyRelatedField(queryset=CourseProgram.objects.all())

    class Meta:
        model = LecturerProfile
        fields = ['id', 'user', 'name', 'email', 'phone', 'program', 'address', 'created_at', 'updated_at']
