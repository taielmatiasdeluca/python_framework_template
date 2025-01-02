#
#   METODOS HTTP, DECORADORES DISEÑADOS PARA CONTROLADORES
#


def get(path):
    def decorador(func):
        func.route_path = path
        func.route_method = "GET"

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result, path, "GET"

        return wrapper

    return decorador


def post(path):
    def decorador(func):
        func.route_path = path
        func.route_method = "POST"

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result, path, "POST"

        return wrapper

    return decorador


def delete(path):
    def decorador(func):
        func.route_path = path
        func.route_method = "DELETE"

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result, path, "DELETE"

        return wrapper

    return decorador


def put(path):
    def decorador(func):
        func.route_path = path
        func.route_method = "PUT"

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result, path, "PUT"

        return wrapper

    return decorador
