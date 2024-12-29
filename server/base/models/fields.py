class Field:
    primary_key = False
    nullable = False
    unique = False
    default = None


class Boolean(Field):
    col_type = "boolean"

    def __init__(self, default=False):
        self.default = default


class Char(Field):
    col_type = "char"

    def __init__(self, max_length=255, default=""):
        self.max_length = max_length
        self.default = default


class Integrer(Field):
    col_type = "integer"

    def __init__(self, default=0):
        self.default = default
