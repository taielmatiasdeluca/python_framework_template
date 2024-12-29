from base.instance import Instance
import modelos
from base.logger import Logger

logger = Logger()


def main():
    # Se inicia el servidor
    server = Instance()
    server.load_models(modelos)
    server.start()


if __name__ == "__main__":
    main()
