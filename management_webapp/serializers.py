from rest_framework import serializers
from management_webapp.models import CourseProgram  # Use singular CourseProgram


class CourseProgramSerializer(serializers.ModelSerializer):  # Use singular CourseProgramSerializer
    class Meta:
        model = CourseProgram
        fields = ['id', 'text']


# class TuitionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tuition
#         fields = ['id', 'text']
