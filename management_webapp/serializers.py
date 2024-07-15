from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CourseProgram, StudentProfile, LecturerProfile, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'phone', 'address', 'profession']

class CourseProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgram
        fields = ['id', 'name', 'description', 'duration', 'tuition_fee']

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    courses = CourseProgramSerializer(many=True, read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'name', 'email', 'phone', 'courses', 'marks', 'address', 'mother_name', 'father_name', 'created_at', 'updated_at']

class LecturerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    program = CourseProgramSerializer(read_only=True)

    class Meta:
        model = LecturerProfile
        fields = ['id', 'user', 'name', 'email', 'phone', 'program', 'address', 'created_at', 'updated_at']
