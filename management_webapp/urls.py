from rest_framework.routers import DefaultRouter
from management_webapp.viewsets import CourseProgramViewSet  # Import viewsets correctly

router = DefaultRouter()
router.register('courseprograms', CourseProgramViewSet, basename='courseprograms')  # Use the correct viewsets
# router.register('tuition', TuitionViewSet, basename='tuition')
urlpatterns = router.urls
