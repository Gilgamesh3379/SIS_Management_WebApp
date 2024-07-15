from django.contrib import admin
from .models import CourseProgram, StudentProfile, LecturerProfile

@admin.register(CourseProgram)
class CourseProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'tuition_fee', 'created_at', 'updated_at')
    search_fields = ('name', 'description')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'marks', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('courses',)

@admin.register(LecturerProfile)
class LecturerProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'program', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('program',)
