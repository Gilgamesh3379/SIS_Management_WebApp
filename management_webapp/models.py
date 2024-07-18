from django.contrib.auth.models import User
from django.db import models

class CourseProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(default=6)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    courses = models.ManyToManyField(CourseProgram, related_name='students')
    marks = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LecturerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer_profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    program = models.ForeignKey(CourseProgram, on_delete=models.CASCADE, related_name='lecturers')
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
