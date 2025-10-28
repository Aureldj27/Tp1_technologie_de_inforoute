from  .views import home
from django.urls import path,include
from django.urls import path
from .views import DatasetListView, DatasetDetailView, HarvestView


urlpatterns = [
    path('',home,name="home"),
    path("datasets/", DatasetListView.as_view(), name="dataset-list"),
    path("datasets/<str:ckan_id>/", DatasetDetailView.as_view(), name="dataset-detail"),
    path("harvest/", HarvestView.as_view(), name="harvest"),

   
]