class Route:
    def __init__(self, method, path, controller):
        self.method = method
        self.path = path
        self.controller = controller

    def __str__(self):
        return f"Ruta: {self.method} {self.path}"
        pass
