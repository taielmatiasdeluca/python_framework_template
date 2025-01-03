# Backend

## Descripción

El backend de este proyecto utiliza sqlite como base de datos, permite crear modelos que se crearan y modificaran en la base de datos.

## Uso

### Modelos

Los modelos se declaran en el archivo `modelos/__init__.py`, y se crean en la base de datos dependiendo de los fields que se declaren.

```python
from base.models import baseModel
from base.models import fields

class Usuario(baseModel.BaseModel): #Instancia el modelo.
    table_name = "usuario" # Nombre de la tabla en la base de datos

    username = fields.Char(length=10) # columnas de la base de datos
    password = fields.Char()
```

### Controladores

Los controladores se declaran en el archivo `controlador/__init__.py`, y se utilizan para crear endpoints.

```python
from base.web.controller import Controller
from base.web.methods import get, post, put, delete

class Main(Controller):

    @get("/") # Permite crear endpoints con el método GET
    def index(request, headers): # Permite recibir los headers y el request
        return "Hola mundo" # Devuelve la respuesta el cliente
```

### Servidor

Para ejecutar el servidor, se debe ejecutar el siguiente comando:

```bash
python3 server.py
```