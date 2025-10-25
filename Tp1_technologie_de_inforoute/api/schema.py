import graphene
from graphene_django import DjangoObjectType
from core.models import Dataset

# ─── DatasetType ───
class DatasetType(DjangoObjectType):
    class Meta:
        model = Dataset
        fields = "__all__"  # Inclut tous les champs du modèle automatiquement

# ─── Fonction pour générer dynamiquement les arguments Graphene à partir du modèle ───
def generate_graphene_fields(model):
    """
    Crée un dictionnaire d'arguments Graphene pour tous les champs d'un modèle Django.
    Les JSONField sont mappés en graphene.JSONString.
    Les champs requis (primary_key) deviennent obligatoires.
    """
    FIELD_MAPPING = {
        "CharField": graphene.String,
        "TextField": graphene.String,
        "EmailField": graphene.String,
        "URLField": graphene.String,
        "IntegerField": graphene.Int,
        "BooleanField": graphene.Boolean,
        "DateTimeField": graphene.DateTime,
        "JSONField": graphene.JSONString,  # GraphQL JSON comme dict/list
    }

    fields = {}
    for field in model._meta.get_fields():
        if field.auto_created:  # Ignore id auto ou relations inverses
            continue
        field_type = type(field).__name__
        graphene_type = FIELD_MAPPING.get(field_type)
        if graphene_type:
            # Rendre obligatoire si primary_key ou non null sans blank
            required = getattr(field, "primary_key", False) or (not getattr(field, "blank", True))
            fields[field.name] = graphene_type(required=required)
    return fields

# ─── Queries ───
class Query(graphene.ObjectType):
    all_datasets = graphene.List(DatasetType)
    dataset_by_ckan_id = graphene.Field(DatasetType, ckan_id=graphene.String(required=True))

    def resolve_all_datasets(root, info, **kwargs):
        return Dataset.objects.all()

    def resolve_dataset_by_ckan_id(root, info, ckan_id):
        try:
            return Dataset.objects.get(ckan_id=ckan_id)
        except Dataset.DoesNotExist:
            return None

# ─── Mutations ───
class Mutation(graphene.ObjectType):
    create_dataset = graphene.Field(DatasetType, **generate_graphene_fields(Dataset))

    def resolve_create_dataset(root, info, **kwargs):
        # JSONFields peuvent être passés comme dict/list directement
        dataset = Dataset(**kwargs)
        dataset.save()
        return dataset

# ─── Schéma GraphQL ───
schema = graphene.Schema(query=Query, mutation=Mutation)
