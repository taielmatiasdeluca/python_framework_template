from base.models import baseModel
from base.models import fields
from base.database.database import Database

class Usuario(baseModel.BaseModel):
    table_name = "usuario"
   

    username = fields.Char(length=10)
    password = fields.Char()
    
    def insert(self, username, password):
        database = Database()
        self.username = username
        self.password = password
        res = database.query(f'INSERT INTO {self.table_name} (username, password) VALUES ("{self.username}", "{self.password}")')
        return 'ok'
         
    
    def get(self):
        database = Database()
        response = database.query(f'SELECT * FROM {self.table_name}')        
        return response.fetchall()
        