from base.web.controller import Controller
from base.web.methods import get, post, put, delete


class User(Controller):

    @get("/")
    def index(self, request):
        return "Hola mundo"