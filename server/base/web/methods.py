#
#   METODOS HTTP, DECORADORES DISEÑADOS PARA CONTROLADORES
#

from ..logger import Logger

logger = Logger()

def http_method(method, path):
    def decorador(func):
        func.route_path = path
        func.route_method = method
        

        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result, 200
            except Exception as e:
                logger.error(e)
        return wrapper

    return decorador




get = lambda path: http_method("GET", path)
post = lambda path: http_method("POST", path)
delete = lambda path: http_method("DELETE", path)
put = lambda path: http_method("PUT", path)
