from base.web.controller import Controller
from base.web.methods import get, post, put, delete


class Main(Controller):

    @get("/main")
    def index(self):
        return "Hola mundo"
