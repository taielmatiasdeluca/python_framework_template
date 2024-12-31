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
                        fields_sql.append(self._prepare_field_query(name, propierty))
            sql = ",\n".join(fields_sql)
            sql = f"CREATE TABLE {table_name} (\n{sql}\n);"
            res = self.database.query(sql)
        else:
            # La tabla existe, verificar que no haya cambios en el modelo
            table_related = next(
                filter(lambda table: table.name == table_name, self.database.tables),
                None,
            )
            add_fields = []
            changes_fields = []
            for name, propierty in vars(objt.__class__).items():
                if not name.startswith("__"):
                    if isinstance(propierty, fields.Field):
                        # Campo dentro de la tabla
                        field = next(
                            (
                                field
                                for field in table_related.fields
                                if field.name == name
                            ),
                            None,
                        )
                        if field:
                            # TODO: implementar cambios en el campo
                            pass
                        else:
                            # Creamos el campo
                            changes_fields.append(
                                self._prepare_create_field_query(name, propierty)
                            )
            # al terminar de calcular los campos, se genera la query correspondiente,

            # Verificamos que no haya campos en la base de datos, que no se utilicen.
            object_fields = [name for name, propierty in vars(objt.__class__).items()]
            for field in table_related.fields:
                if not field.name in object_fields:
                    # Se encontro un campo que tiene que ser eliminado.
                    changes_fields.append(self._prepare_delete_field_query(field.name))

            if changes_fields:
                sql = ",\n".join(changes_fields)
                sql = f"ALTER TABLE {table_name} \n{sql};"
                logger.info(
                    f'Se detectaron cambios sobre el modelo "{table_name}", se ejecuta la siguiente query {sql}'
                )
                res = self.database.query(sql)

    def _prepare_delete_field_query(self, col_name):
        # Elimina el campo de la tabla.
        query = f"DROP COLUMN {col_name}"
        return query

    def _prepare_create_field_query(self, col_name, propierty, edit=0):
        # TODO: implementar mas opciones, null default, etc.
        length = f"({propierty.length})" if propierty.length else ""
        col_type = propierty.col_type
        primary_key = propierty.primary_key

        query = f"ADD {col_name} {col_type}{length}"
        return query

    def _prepare_modify_field_query(self, col_name, propierty, edit=0):
        # TODO: implementar mas opciones, null default, etc.
        col_type = propierty.col_type
        primary_key = propierty.primary_key
        length = f"({propierty.length})" if propierty.length else ""
        query = f"MODIFY COLUMN {col_name} {col_type}{length}"
        return query

    def _prepare_field_query(self, col_name, propierty, edit=0):
        # TODO: implementar mas opciones, null default, etc.
        col_type = propierty.col_type
        primary_key = "PRIMARY KEY" if propierty.primary_key else ""
        propierty_query = f"{col_name} {col_type} {primary_key}"
        return propo
