import MySQLdb
from django.conf import settings

db = MySQLdb.connect(
    host=settings.DATABASES['default']['HOST'] or 'localhost',
    user=settings.DATABASES['default']['USER'],
    passwd=settings.DATABASES['default']['PASSWORD']
)

cursor = db.cursor()
db_name = settings.DATABASES['default']['db_tp1_technologie_inforoute']

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
print(f"✅ Base de données '{db_name}' créée (ou déjà existante).")

cursor.close()
db.close()
