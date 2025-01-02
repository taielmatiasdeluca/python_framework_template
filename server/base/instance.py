from .logger import Logger
from .database.database import Database
from .web.webServer import WebServer
from .web.routes.mainRouter import MainRouter

import inspect
from dotenv import load_dotenv
logger = Logger()
load_dotenv()




class Instance:
    def __init__(self):
        logger.info("Iniciando Instancia")
        self.database = Database()
        self.mainRouter = MainRouter()
        

    def start(self):
        webServer = WebServer()
        webServer.mainRouter = self.mainRouter
        webServer.start()
        

    def load_models(self, models):
        # Levantan los modelos declarados en el backend, y se cargan o modifican en la base de datos.
        models_to_init = [elem for elem in dir(models) if not elem.startswith("__")]
        for nombre_objeto, model_obj in models.__dict__.items():
            if nombre_objeto in models_to_init:
                for nombre, obj in vars(model_obj).items():
                    if isinstance(obj, type):  # Verifica si el atributo es una clase
                        modelo = obj()
                        modelo._make_migrations(modelo)

    def load_controllers(self, controllers):
        # Se levantan los controladores de tipo get, post, etc.
        # Levantan los modelos declarados en el backend, y se cargan o modifican en la base de datos.
        self.mainRouter.init(controllers)
