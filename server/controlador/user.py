from base.web.controller import Controller
from base.web.methods import get, post, put, delete
from base.template.engine import TemplateEngine
import json
from modelos.Usuario import Usuario
from base.logger import Logger

logger = Logger()

class User(Controller):

    @get("/")
    def index(request, headers):
        template = TemplateEngine('vistas/index.html')
        userModel = Usuario()
        usuarios = userModel.get()
        table = " ".join([f'<tr><td>{usuario[0]}</td><td>{usuario[1]}</td></tr>' for usuario in usuarios])
        template.setVariable('user_table', table)
        return template.render()
    
    @post("/insert")
    def insert(headers, body):
        try:
            data = json.loads(str(body))
            userModel = Usuario()
            if userModel.insert(data['username'], data['password']):
                return 'ok'
        except Exception as e:
            logger.error(e)
            return 'error'
    