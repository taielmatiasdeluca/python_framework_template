from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


CONSOLE_COLORS = {
    "ERROR": "\033[31m",
    "SUCCESS": "\033[32m",
    "WARNING": "\033[38;2;255;165;0m",
    "INFO": "\033[33m",
    "RESET": "\033[0m",
}


LOG_FILE = False
if os.getenv("LOG_FILE"):
    LOG_FILE = str(os.getenv("LOG_FILE"))


class Logger:
    _instance = None

    def __new__(cls):
        # Permite reutilizar la instancia del logger en memoria al utilizarlo
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.init_instance_time = datetime.now()

    def warning(self, message):
        """
        Imprime un mensaje de advertencia de color amarillo en la consola.

        Parameters:
        message (str): El mensaje a imprimir.
        """
        self._print_line_with_color(message, "WARNING")

    def info(self, message):
        """
        Imprime un mensaje de información de color azul en la consola.

        Parameters:
        message (str): El mensaje a imprimir.
        """
        self._print_line_with_color(message, "INFO")

    def success(self, message):
        """
        Imprime un mensaje de éxito de color verde en la consola.

        Parameters:
        message (str): El mensaje a imprimir.
        """
        self._print_line_with_color(message, "SUCCESS")

    def error(self, message):
        """
        Imprime un mensaje de error de color rojo en la consola.

        Parameters:
        message (str): El mensaje a imprimir.
        """
        self._print_line_with_color(message, "ERROR")

    def _print_line_with_color(self, message, type):
        """
        Imprime un mensaje en la consola con el color especificado.

        Parameters:
        message (str): El mensaje a imprimir.
        color (str): El color del mensaje.
        """
        if LOG_FILE:
            with open(LOG_FILE, "a") as f:
                f.write(f"[SERVER] {str(type).upper()}: {message}\n")
        print(
            f"{CONSOLE_COLORS[type]}[SERVER] {str(type).upper()}: {message}{CONSOLE_COLORS['RESET']}"
        )

    def log_execution(self, func):
        def wrapper(*args, **kwargs):
            self.info(f"Se ejecutó la función: {func.__name__}")
            return func(*args, **kwargs)

        return wrapper
