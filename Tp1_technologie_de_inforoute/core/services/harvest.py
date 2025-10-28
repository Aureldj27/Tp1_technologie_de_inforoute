import requests
from django.utils import timezone
from core.models import Dataset  # ✅ Utilisation de ton modèle

CKAN_API_URL = "https://www.donneesquebec.ca/recherche/api/3/action/"

def harvest_datasets(keyword: str, rows: int = 50):
    """
    Récupère les jeux de données depuis Données Québec pour un mot-clé donné.
    Stocke les datasets dans la base si ils n'existent pas ou les met à jour.
    """
    params = {"q": keyword, "rows": rows, "start": 0}
    response = requests.get(CKAN_API_URL + "package_search", params=params)
    data = response.json()

    if not data.get("success"):
        raise Exception(f"Erreur API CKAN : {data}")

    results = data["result"]["results"]
    datasets = []

    for item in results:
        obj, created = Dataset.objects.update_or_create(
            ckan_id=item.get("id"),
            defaults={
                "name": item.get("name"),
                "title": item.get("title"),
                "notes": item.get("notes"),
                "organization_title": item.get("organization", {}).get("title") if item.get("organization") else None,
                "tags": [t.get("name") for t in item.get("tags", [])],
                "metadata_created": item.get("metadata_created"),
                "metadata_modified": item.get("metadata_modified"),
                "last_harvested": timezone.now(),
            },
        )
        datasets.append(obj)
    return datasets
