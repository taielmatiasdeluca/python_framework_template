class StaticFile:
    def __init__(self, path, content):
        self.path = path
        self.content = content

    def read(self, headers, request):
        return self.content, 200
