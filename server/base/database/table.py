class Table:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    def __str__(self):
        str = f"Tabla: {self.name}\n"
        for field in self.fields:
            str += f"\t{field}"
        return str
