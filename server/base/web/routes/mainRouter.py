from ..routes.route import Route
from ..controller import Controller


# Clase general que detecta las rutas y divide las peticiones segun estas
class MainRouter:
    # Generamos propiedad principal que contiene las rutas
    routes = {"GET": [], "POST": [], "PUT": [], "DELETE": []}

    def __init__(self):
        pass

    def init(self, controllers):
        """
        Levanta las diferentes rutas de los controladores, y las almacena en una lista, para luego procesar las peticiones.
        """
        controllers_to_init = [
            elem for elem in dir(controllers) if not elem.startswith("__")
        ]
        # Se listan los archivos dentro del modulo
        for nombre_file, controller_obj in controllers.__dict__.items():
            # Solo si el nombre de los archivos enta entre los filtrados
            if nombre_file in controllers_to_init:
                # Listamos los objetos dentro del archivo
                for nombre, obj in vars(controller_obj).items():
                    # Filtramos las clases que son son el "controlador literal"
                    if isinstance(obj, type) and obj is not Controller:
                        # Obtén solo los métodos definidos en la clase actual
                        for method_name, func in obj.__dict__.items():
                            if callable(func):
                                print(func)
                                for cell in func.__closure__:
                                    if hasattr(cell.cell_contents, "route_path"):
                                        original_func = cell.cell_contents
                                        break
                                path = original_func.route_path
                                method = original_func.route_method
                                self.routes[method].append(
                                    Route(path, obj, method_name)
                                )
        print(self.routes)
