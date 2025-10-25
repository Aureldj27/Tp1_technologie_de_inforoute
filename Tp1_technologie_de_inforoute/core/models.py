from django.db import models

class Dataset(models.Model):
    # ─── Identifiants et métadonnées de base ───
    ckan_id = models.CharField(
        max_length=36,
        primary_key=True,
        help_text="Identifiant unique CKAN du jeu de données"
    )
    name = models.CharField(
        max_length=255,
        db_index=True,
        help_text="Nom interne (slug) du jeu de données"
    )
    title = models.CharField(
        max_length=500,
        help_text="Titre lisible du jeu de données"
    )

    # ─── Description et contact ───
    notes = models.TextField(
        blank=True, null=True,
        help_text="Description ou résumé du jeu de données"
    )
    author = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Auteur ou producteur du jeu"
    )
    author_email = models.EmailField(
        blank=True, null=True,
        help_text="Courriel de l’auteur ou producteur"
    )
    maintainer = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Responsable du jeu de données"
    )
    maintainer_email = models.EmailField(
        blank=True, null=True,
        help_text="Courriel du responsable"
    )

    # ─── Organisation associée ───
    organization_id = models.CharField(
        max_length=36, blank=True, null=True, db_index=True,
        help_text="Identifiant de l’organisation propriétaire"
    )
    organization_title = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Nom de l’organisation propriétaire"
    )

    # ─── Licence, langue, etc. ───
    language = models.CharField(
        max_length=10, blank=True, null=True,
        help_text="Langue du jeu de données (ex : 'fr', 'en')"
    )
    license_id = models.CharField(
        max_length=50, blank=True, null=True,
        help_text="Identifiant de la licence (ex : 'cc-by')"
    )
    license_title = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Titre lisible de la licence"
    )
    license_url = models.URLField(
        blank=True, null=True,
        help_text="URL de la licence"
    )

    # ─── Dates de métadonnées ───
    metadata_created = models.DateTimeField(
        blank=True, null=True,
        help_text="Date de création des métadonnées"
    )
    metadata_modified = models.DateTimeField(
        blank=True, null=True,
        help_text="Date de dernière modification des métadonnées"
    )

    # ─── Temporalité et mise à jour ───
    temporal = models.CharField(
        max_length=100, blank=True, null=True,
        help_text="Couverture temporelle (ex : période du jeu de données)"
    )
    update_frequency = models.CharField(
        max_length=50, blank=True, null=True,
        help_text="Fréquence de mise à jour du jeu de données"
    )

    # ─── Statut, confidentialité ───
    state = models.CharField(
        max_length=50, blank=True, null=True,
        help_text="État du jeu de données (ex : 'active', 'deleted')"
    )
    private = models.BooleanField(
        default=False,
        help_text="Indique si le jeu de données est privé"
    )

    # ─── Tags, groupes et catégorisation ───
    tags = models.JSONField(
        blank=True, null=True,
        help_text="Liste de mots-clés associés au jeu de données"
    )
    groups = models.JSONField(
        blank=True, null=True,
        help_text="Liste de groupes ou thèmes associés au jeu de données"
    )

    # ─── Champs additionnels / extension du modèle ───
    num_resources = models.IntegerField(
        blank=True, null=True,
        help_text="Nombre de ressources contenues dans le jeu de données"
    )
    url = models.URLField(
        blank=True, null=True,
        help_text="Lien vers la fiche ou la page du jeu de données"
    )
    last_harvested = models.DateTimeField(
        blank=True, null=True,
        help_text="Date à laquelle le jeu a été importé dans le système"
    )

    def __str__(self):
        return f"{self.title} ({self.name})"
