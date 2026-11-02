from django.db.backends.mysql import base as mysql_base
from django.db.backends.mysql.features import DatabaseFeatures as MySQLDatabaseFeatures

class DatabaseFeatures(MySQLDatabaseFeatures):
    # MariaDB 10.4 não suporta a cláusula RETURNING no SQL. Desativamos para usar lastrowid.
    can_return_columns_from_insert = False

class DatabaseWrapper(mysql_base.DatabaseWrapper):
    features_class = DatabaseFeatures

    def check_database_version_supported(self):
        # Bypassa a verificação de versão mínima do MariaDB para permitir MariaDB 10.4 no XAMPP com Django 6.x
        pass
