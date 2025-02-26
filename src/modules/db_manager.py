import sqlite3

class LootDatabase:
    def __init__(self, db_name='loot_database.db'):
        self.db_name = db_name
        self.initialize_database()

    def initialize_database(self):
        # Connexion à la base de données (ou création si elle n'existe pas)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Création de la table 'loot'
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS loot (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                uuid TEXT NOT NULL UNIQUE,
                checked BOOLEAN NOT NULL
            )
        ''')

        # Commit et fermeture de la connexion
        conn.commit()
        conn.close()

    def get_loot_by_uuid(self, uuid):
        # Connexion à la base de données
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Requête pour récupérer les informations en fonction de l'UUID
        cursor.execute('''
            SELECT name, checked
            FROM loot
            WHERE uuid = ?
        ''', (uuid,))

        # Récupération du résultat
        loot_info = cursor.fetchone()

        # Fermeture de la connexion
        conn.close()

        # Retourne les informations sous forme de dictionnaire si trouvé, sinon None
        if loot_info:
            return {
                'name': loot_info[0],
                'checked': bool(loot_info[1])
            }
        else:
            return None

    def set_loot_checked_by_uuid(self, uuid):
        # Connexion à la base de données
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Requête pour mettre à jour le champ 'checked' à 1 en fonction de l'UUID
        cursor.execute('''
            UPDATE loot
            SET checked = 1
            WHERE uuid = ?
        ''', (uuid,))

        # Commit et fermeture de la connexion
        conn.commit()
        conn.close()

    def reset_loot_checked_by_uuid(self, uuid):
        # Connexion à la base de données
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Requête pour réinitialiser le champ 'checked' à 0 en fonction de l'UUID
        cursor.execute('''
            UPDATE loot
            SET checked = 0
            WHERE uuid = ?
        ''', (uuid,))

        # Commit et fermeture de la connexion
        conn.commit()
        conn.close()