from django.db import models

class Dataset(models.Model):
    # Identifiants
    ckan_id = models.CharField(max_length=36, primary_key=True)  # UUID CKAN
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    
    # Description et informations générales
    notes = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    author_email = models.EmailField(blank=True, null=True)
    maintainer = models.CharField(max_length=255, blank=True, null=True)
    maintainer_email = models.EmailField(blank=True, null=True)
    
    # Organisation
    organization_id = models.CharField(max_length=36, blank=True, null=True)
    organization_title = models.CharField(max_length=255, blank=True, null=True)
    
    # Informations complémentaires
    language = models.CharField(max_length=10, blank=True, null=True)
    license_id = models.CharField(max_length=50, blank=True, null=True)
    license_title = models.CharField(max_length=255, blank=True, null=True)
    license_url = models.URLField(blank=True, null=True)
    
    # Dates
    metadata_created = models.DateTimeField(blank=True, null=True)
    metadata_modified = models.DateTimeField(blank=True, null=True)
    
    # Fréquence et temporalité
    temporal = models.CharField(max_length=100, blank=True, null=True)
    update_frequency = models.CharField(max_length=50, blank=True, null=True)
    
    # Statut et confidentialité
    state = models.CharField(max_length=50, blank=True, null=True)
    private = models.BooleanField(default=False)
    
    # Tags et groupes stockés en JSON
    tags = models.JSONField(blank=True, null=True)   # liste de tags
    groups = models.JSONField(blank=True, null=True) # liste de groupes / catégories

    def __str__(self):
        return f"{self.title} ({self.name})"