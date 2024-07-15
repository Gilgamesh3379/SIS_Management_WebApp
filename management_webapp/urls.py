from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CourseProgramViewSet, StudentProfileViewSet, LecturerProfileViewSet

router = DefaultRouter()
router.register('courseprograms', CourseProgramViewSet)
router.register('studentprofiles', StudentProfileViewSet)
router.register('lecturerprofiles', LecturerProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
