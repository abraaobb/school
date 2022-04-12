from rest_framework.routers import DefaultRouter
from basic import viewsets

router = DefaultRouter()
router.register('course', viewset=viewsets.CourseViewSet)

urlpatterns = router.urls
