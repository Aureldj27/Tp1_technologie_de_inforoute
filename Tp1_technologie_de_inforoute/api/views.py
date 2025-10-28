from core.models import Dataset
from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.services.harvest import harvest_datasets  # ← nouvel import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import DatasetSerializer



# Liste tous les datasets
class DatasetListView(generics.ListAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

# Détail d'un dataset
class DatasetDetailView(generics.RetrieveAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    lookup_field = "ckan_id"  # on peut chercher par ckan_id

class HarvestView(APIView):
    authentication_classes = []  # désactive session auth pour éviter 403
    permission_classes = []      # ou [AllowAny]

    def post(self, request):
        keyword = request.data.get("keyword")
        if not keyword:
            return Response({"error": "Le mot-clé est requis."}, status=status.HTTP_400_BAD_REQUEST)

        datasets = harvest_datasets(keyword)  # sauvegarde dans DB
        serializer = DatasetSerializer(datasets, many=True)
        return Response({
            "count": len(datasets),
            "results": serializer.data
        }, status=status.HTTP_200_OK)


def home(request):
	return HttpResponse("<html><body><p> je suis fans api</p></body></html>")