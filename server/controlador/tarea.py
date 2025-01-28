from base.web.controller import Controller
from base.web.methods import get, post, put, delete
from base.template.engine import TemplateEngine
import json
from modelos.Tareas import Tareas
from base.logger import Logger

logger = Logger()


class Tarea(Controller):
    @get("/")
    @logger.log_execution
    def index(request, headers):
        template = TemplateEngine("vistas/index.html")
        tareaModel = Tareas()
        usuarios = tareaModel.get()
        table = " ".join(
            [
                f"<tr><td>{usuario[0]}</td><td>{usuario[1]}</td></tr>"
                for usuario in usuarios
            ]
        )
        template.setVariable("todo_list", table)
        return template.render()

    @post("/insert")
    @logger.log_execution
    def insert(headers, body):
        try:
            data = json.loads(str(body))
            tareaModel = Tareas()
            if tareaModel.insert(data["titulo"], data["descripcion"]):
                return "ok"
        except Exception as e:
            logger.error(e)
            return "error"
