class Field:
    def __init__(self, name, type, primary_key=False, unique=False):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.unique = unique

    def __str__(self):
        str = f"Campo: {self.name}"
        str += f"\tTipo: {self.type}"
        if self.primary_key:
            str += "\tCampo Primario"
        if self.unique:
            str += "\tCampo Único"
        str += "\n"
        return str
