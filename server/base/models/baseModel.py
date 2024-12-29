from ..database.database import Database
from ..logger import Logger
from . import model

logger = Logger()


class BaseModel(model.Model):
    def __init__(self):

        pass
