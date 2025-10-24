import os
import configparser
from django.core.management.base import BaseCommand
import MySQLdb

# Si ton script est dans un sous-dossier, ajuste BASE_DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class Command(BaseCommand):
    help = "Crée la base de données définie dans my.conf (si elle n'existe pas déjà)."

    def handle(self, *args, **options):
        # Lire le fichier my.conf
        config_path = os.path.join(BASE_DIR, "my.conf")
        if not os.path.exists(config_path):
            self.stderr.write(self.style.ERROR(f"❌ Fichier my.conf introuvable à {config_path}"))
            return

        config = configparser.ConfigParser()
        config.read(config_path)

        try:
            db_name = config.get('client', 'database')
            user = config.get('client', 'user')
            password = config.get('client', 'password')
            host = config.get('client', 'host', fallback='localhost')

            if not db_name:
                self.stderr.write(self.style.ERROR("❌ Le nom de la base de données est vide dans my.conf"))
                return

            self.stdout.write(self.style.NOTICE(f"Connexion à MySQL ({user}@{host})..."))
            db = MySQLdb.connect(host=host, user=user, passwd=password)
            cursor = db.cursor()

            # Créer la base si elle n'existe pas
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS `{db_name}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
            )

            self.stdout.write(self.style.SUCCESS(f"✅ Base de données '{db_name}' créée (ou déjà existante)."))

        except configparser.NoOptionError as e:
            self.stderr.write(self.style.ERROR(f"❌ Option manquante dans my.conf : {e}"))
        except MySQLdb.Error as e:
            self.stderr.write(self.style.ERROR(f"❌ Erreur MySQL : {e}"))
        finally:
            try:
                cursor.close()
                db.close()
            except Exception:
                pass
