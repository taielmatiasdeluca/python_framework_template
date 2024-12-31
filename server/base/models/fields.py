from ..logger import Logger
from ..utils.values import *

logger = Logger()


class Field:
    primary_key = False
    col_type = "varchar"
    nullable = False
    unique = False
    default = None
    length = Length()


class Boolean(Field):
    col_type = "boolean"
    default = Boolean()

    def __init__(self, default=False):
        self.default = default


class Char(Field):
    col_type = "varchar"

    def __init__(self, length=255, default=""):
        self.length = length
        self.default = default


class Integrer(Field):
    col_type = "integer"

    def __init__(self, length=0, default=0):
        self.length = length
        self.default = default
