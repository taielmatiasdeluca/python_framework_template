import socket
import threading
import time
import os
from dotenv import load_dotenv


from ..logger import Logger

load_dotenv()

PORT = os.getenv("WEB_PORT")


logger = Logger()


class WebServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not PORT:
            logger.error("WEB_PORT no configurado sobre .env")
            return
        try:
            self.server.bind(("", int(PORT)))
            self.server.listen(1)
        except Exception as e:
            logger.error(e)
            logger.error("Error al iniciar el servidor web")

    def start(self):
        server_thread = threading.Thread(target=self.run)
        server_thread.start()
        logger.success(f"Servidor iniciado en segundo plano sobre el puerto {PORT}")
        # Mantener el programa principal en ejecución
        while True:
            time.sleep(1)

    def run(self):
        while True:
            conn, addr = self.server.accept()
            logger.info(f"Se ha conectado con {addr}")
            thread = threading.Thread(target=self.handle_client, args=(conn,))
            thread.start()

    def handle_client(self, conn):
        try:
            data = conn.recv(1024).decode()
            response = "HTTP/1.1 200 OK\n\nHello from the server!"
            conn.sendall(response.encode())
        except Exception as e:
            logger.error(f"Error al manejar la conexión: {e}")
        finally:
            conn.close()
