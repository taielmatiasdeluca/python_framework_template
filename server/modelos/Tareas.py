from base.models import baseModel
from base.models import fields
from base.database.database import Database


class Tareas(baseModel.BaseModel):
    table_name = "tareas"

    titulo = fields.Char()
    descripcion = fields.Char()

    def insert(self, titulo, descripcion):
        database = Database()
        self.titulo = titulo
        self.descripcion = descripcion
        res = database.query(
            f'INSERT INTO {self.table_name} (titulo, descripcion) VALUES ("{self.titulo}", "{self.descripcion}")'
        )
        return "ok"

    def get(self):
        database = Database()
        response = database.query(f"SELECT * FROM {self.table_name}")
        return response.fetchall()
