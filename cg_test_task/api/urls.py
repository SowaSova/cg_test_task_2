from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet, JobRelationViewSet

app_name = "api"

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"job_titles", JobRelationViewSet, basename="job_title")

urlpatterns = [
    path("", include(router.urls)),
]
