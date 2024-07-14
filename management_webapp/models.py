from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourseProgram(models.Model):  # Rename to singular for consistency
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


# class Tuition(models.Model):
#     text = models.TextField()
#     course_program = models.ForeignKey(CourseProgram, on_delete=models.CASCADE)  # Link to the correct model
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.text
