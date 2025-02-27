import sqlite3
import os

from ..logger import Logger

from dotenv import load_dotenv
from .field import Field
from .table import Table

load_dotenv()


BD_FILE = "./" + str(os.getenv("DB_FILE"))

logger = Logger()

# TODO: base de datos no implementa funcionalidad SINGLETON ya que sqlite3 no soporta utilizacion sobre multiples sockets.


class Database:
    _instance = None

    def __init__(self):
        logger.info("Iniciando Base de Datos")
        try:
            self.conn = sqlite3.connect(BD_FILE)
            self.cursor = self.conn.cursor()
            self.tables = self._init_tables()
            logger.success("Cliente de base de datos inicializado")

        except Exception as e:
            logger.error(f"Error al iniciar la base de datos: {e}")

    def query(self, query):
        try:
            res = self.cursor.execute(query)
            self.conn.commit()
            return res
        except Exception as e:
            logger.error(str(e))
            logger.error(f"Error al ejecutar la consulta: '{query}'")

    def fetchAll(self, query):
        try:
            res = self.conn.execute(query)
            return res.fetchall()
        except Exception as e:
            logger.error(str(e))
            logger.error(f"Error al ejecutar la consulta: '{query}'")

    def _init_tables(self):
        """
        Se devuelven las tablas que se encuentran en la bd con sus campos.
        """
        tables = []
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            for table in self.cursor.fetchall():
                table_name = table[0]
                fields = []
                self.cursor.execute(f"PRAGMA table_info({table_name})")
                for field in self.cursor.fetchall():
                    fields.append(Field(field[1], field[2]))
                tables.append(Table(table_name, fields))
            logger.info(
                f"Se encontraron un total de {len(tables)} tablas en la base de datos"
            )
        except Exception as e:
            logger.error(str(e))
            logger.error("Error al obtener las tablas de la bd")
        return tables
