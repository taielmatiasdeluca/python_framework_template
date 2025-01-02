class Route:
    def __init__(self, path, obj, method):
        self.path = path
        self.obj = obj
        self.method = method

    def __str__(self):
        return f"Ruta: {self.method} {self.path}"
        pass
