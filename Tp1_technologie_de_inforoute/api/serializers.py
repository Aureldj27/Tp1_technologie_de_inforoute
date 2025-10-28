# api/serializers.py
from rest_framework import serializers
from core.models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = [
            "ckan_id",
            "name",
            "title",
            "notes",
            "organization_title",
            "tags",
            "metadata_created",
            "metadata_modified",
            "last_harvested",
        ]
