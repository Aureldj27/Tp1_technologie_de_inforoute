from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = [
            'ckan_id', 'name', 'title', 'notes', 'author',
            'organization_title', 'license_title', 'metadata_created',
            'metadata_modified', 'state', 'private', 'tags', 'groups'
        ]