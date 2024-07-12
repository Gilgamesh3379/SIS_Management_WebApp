from django.contrib import admin

from management_webapp.models import UserProfile, CourseProgram, Tuition

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CourseProgram)
admin.site.register(Tuition)
