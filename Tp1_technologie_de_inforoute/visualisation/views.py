from core.models import Dataset
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .forms import SearchForm
from core.services.harvest import harvest_datasets  # ← nouvel import



API_HARVEST_URL = "http://127.0.0.1:8000/api/harvest/"
API_DATASETS_URL = "http://127.0.0.1:8000/api/datasets/"


# views.py
from django.shortcuts import render
from .forms import SearchForm
import requests

def search_view(request):
    datasets = []
    error = None
    form = SearchForm(request.POST or None)  # Création du formulaire, POST si disponible

    if request.method == "POST" and form.is_valid():
        keyword = form.cleaned_data['keyword']

        try:
            # On appelle l'API locale HarvestView
            resp = requests.post(
                'http://127.0.0.1:8000/api/harvest/',
                json={'keyword': keyword},  # en JSON plutôt qu'en data pour DRF
                headers={'Content-Type': 'application/json'}  # bien préciser JSON
            )
            resp.raise_for_status()  # déclenche une exception si erreur HTTP
            data = resp.json()

            # DRF renvoie un dict avec "count" et "results"
            datasets = data.get("results", [])

        except requests.exceptions.RequestException as e:
            error = f"Erreur lors de la récupération des données : {str(e)}"
    elif request.method == "POST":
        error = "Veuillez saisir un mot-clé valide."

    return render(request, 'search.html', {
        'form': form,
        'datasets': datasets,
        'error': error
    })
def home(request):
	return HttpResponse("<html><body><p> je suis fans visualisation</p></body></html>")