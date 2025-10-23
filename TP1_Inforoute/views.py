from rest_framework import viewsets
from .models import Dataset
from .serializers import DatasetSerializer
from rest_framework import filters

class DatasetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'notes', 'tags', 'organization_title']
    ordering_fields = ['metadata_modified', 'title']