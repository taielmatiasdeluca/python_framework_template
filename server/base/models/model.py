from ..database.database import Database
from ..logger import Logger

from ..models import fields

logger = Logger()


class Model:
    database = Database()

    id = fields.Integrer()

    def _make_migrations(self, objt):
        class_name = objt.__class__.__name__
        if not hasattr(objt, "table_name"):
            logger.error(
                f"No se declaro el nombre de la tabla, en el modelo{class_name}"
            )
        try:
            table_name = str(objt.table_name)
            self._create_or_update_table(objt)

        except Exception as e:
            logger.error(e)
            logger.error(f"Error creando las migraciones sobre el modelo {class_name}")

    def _create_or_update_table(self, objt):
        table_name = str(objt.table_name)
        # Create tables
        if table_name not in list(map(lambda table: table.name, self.database.tables)):
            # Se procede a crear la tabla
            fields_sql = []
            for name, propierty in vars(objt.__class__).items():
                if not name.startswith("__"):
                    if isinstance(propierty, fields.Field):
                        col_type = propierty.col_type
                        primary_key = "PRIMARY KEY" if propierty.primary_key else ""

                        propierty_query = f"{name} {col_type} {primary_key}"
                        fields_sql.append(propierty_query)
            sql = ",\n".join(fields_sql)
            sql = f"CREATE TABLE {table_name} (\n{sql}\n);"
            res = self.database.query(sql)
            print(res)
        else:
            # La tabla existe, verificar que no haya cambios en el modelo
            table_related = next(
                filter(lambda table: table.name == table_name, self.database.tables),
                None,
            )
            print(table_related)
