class Controller:
    def __init__(self, method, path):
        self.method = method
        self.path = path

    def not_found(self):
        return "Not Found", 404
