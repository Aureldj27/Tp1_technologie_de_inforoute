from rest_framework import serializers
from .models import Dataset, Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'format', 'url', 'resource_type']


class DatasetSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = [
            'ckan_id', 'name', 'title', 'notes', 'author',
            'organization_title', 'license_title', 'metadata_created',
            'metadata_modified', 'state', 'private', 'tags', 'groups', 'resources'
        ]