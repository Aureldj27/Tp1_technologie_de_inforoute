import requests
from django.core.management.base import BaseCommand
from TP1_Inforoute.models import Dataset
from django.utils.dateparse import parse_datetime

CKAN_BASE_URL = "https://www.donneesquebec.ca/recherche/api/3/action"

class Command(BaseCommand):
    help = "Moissonne les jeux de données depuis donneesquebec.ca"

    def handle(self, *args, **options):
        self.stdout.write("Début du moissonnage CKAN...")

        # Étape 1 : récupérer la liste des datasets
        list_url = f"{CKAN_BASE_URL}/package_list"
        response = requests.get(list_url)
        if not response.ok:
            self.stdout.write(self.style.ERROR("Erreur lors de la récupération de la liste des packages"))
            return

        dataset_names = response.json().get("result", [])

        for name in dataset_names[:50]:  # limiter pour test
            show_url = f"{CKAN_BASE_URL}/package_show?id={name}"
            r = requests.get(show_url)
            if not r.ok:
                continue

            data = r.json().get("result", {})
            dataset, created = Dataset.objects.update_or_create(
                ckan_id=data.get("id"),
                defaults={
                    "name": data.get("name"),
                    "title": data.get("title"),
                    "notes": data.get("notes"),
                    "author": data.get("author"),
                    "author_email": data.get("author_email"),
                    "organization_id": (data.get("organization") or {}).get("id"),
                    "organization_title": (data.get("organization") or {}).get("title"),
                    "license_id": data.get("license_id"),
                    "license_title": data.get("license_title"),
                    "license_url": data.get("license_url"),
                    "metadata_created": parse_datetime(data.get("metadata_created")),
                    "metadata_modified": parse_datetime(data.get("metadata_modified")),
                    "state": data.get("state"),
                    "private": data.get("private", False),
                    "tags": [t["display_name"] for t in data.get("tags", [])],
                    "groups": [g["display_name"] for g in data.get("groups", [])],
                },
            )

            action = "Créé" if created else "Mis à jour"
            self.stdout.write(f"✔ {action} : {dataset.title}")

        self.stdout.write(self.style.SUCCESS("✅ Moissonnage terminé avec succès !"))