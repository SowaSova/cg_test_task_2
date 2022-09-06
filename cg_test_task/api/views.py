from api.serializers import EmployeeSerializer, JobRelationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from employees.models import Employee, JobRelation
from rest_framework import filters, pagination, viewsets

EMPLOYEE_MODEL_FIELDS = ("name", "post", "employment_date", "salary")

JOBRELATION_MODEL_FIELD = ("job_title", "supervisor")


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = EMPLOYEE_MODEL_FIELDS
    search_fields = EMPLOYEE_MODEL_FIELDS
    ordering_fields = EMPLOYEE_MODEL_FIELDS


class JobRelationViewSet(viewsets.ModelViewSet):
    queryset = JobRelation.objects.all()
    serializer_class = JobRelationSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = JOBRELATION_MODEL_FIELD
    search_fields = JOBRELATION_MODEL_FIELD
    ordering_fields = JOBRELATION_MODEL_FIELD
