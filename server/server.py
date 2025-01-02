from base.instance import Instance
import modelos
import controlador
from base.logger import Logger

logger = Logger()


def main():
    # Se inicia el servidor
    server = Instance()
    server.load_models(modelos)
    server.load_controllers(controlador)
    server.start()


if __name__ == "__main__":
    main()
