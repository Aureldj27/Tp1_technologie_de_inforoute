import requests
from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import Dataset  # adapte selon ton app

class Command(BaseCommand):
    help = "Moissonne les métadonnées des jeux de données depuis Données Québec"

    CKAN_API_URL = "https://www.donneesquebec.ca/recherche/api/3/action/"

    def handle(self, *args, **options):
        self.stdout.write("🔍 Lancement de la moisson des jeux de données…")

        # Exemple : recherche des jeux avec un mot-clé spécifique (tu peux adapter)
        params = {
            "q": "transport",  # mot-clé ou filtre il faut trouver tous les mots clé que nous voulons
            "rows": 50,
            "start": 0,
        }
        response = requests.get(self.CKAN_API_URL + "package_search", params=params)
        data = response.json()

        if not data.get("success"):
            self.stderr.write("❌ Échec de l’appel API : %s" % data)
            return

        results = data["result"]["results"]
        count = 0

        for item in results:
            dataset_id = item.get("id")
            name = item.get("name")
            title = item.get("title")

            # Crée ou met à jour l’objet
            obj, created = Dataset.objects.update_or_create(
                ckan_id=dataset_id,
                defaults={
                    "name": name,
                    "title": title,
                    "notes": item.get("notes"),
                    "author": item.get("author"),
                    "author_email": item.get("author_email"),
                    "maintainer": item.get("maintainer"),
                    "maintainer_email": item.get("maintainer_email"),
                    "organization_id": item.get("owner_org"),
                    "organization_title": item.get("organization", {}).get("title") if item.get("organization") else None,
                    "license_id": item.get("license_id"),
                    "metadata_created": item.get("metadata_created"),
                    "metadata_modified": item.get("metadata_modified"),
                    "state": item.get("state"),
                    "private": item.get("private", False),
                    "tags": [t.get("name") for t in item.get("tags", [])],
                    "groups": [g.get("name") for g in item.get("groups", [])],
                    "last_harvested": timezone.now(),
                }
            )
            count += 1
            self.stdout.write(f"- {('Créé' if created else 'Mis à jour')}: {title} (ID={dataset_id})")

        self.stdout.write(self.style.SUCCESS(f"✅ Moissonnage terminé : {count} jeux traités"))
