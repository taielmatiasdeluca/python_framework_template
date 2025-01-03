import socket
import threading
import time
import os
from dotenv import load_dotenv
import signal
from ..logger import Logger
import json

load_dotenv()

PORT = os.getenv("WEB_PORT")


logger = Logger()


class WebServer:
    mainRouter = None

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
            self.stop_server()
            
    def stop_server(self, signum=False, frame=False):
        self.server.close()
        exit(0)
        
        

    def start(self):
        server_thread = threading.Thread(target=self.run)
        signal.signal(signal.SIGINT, self.stop_server)
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
            request = conn.recv(1024).decode()
            # Separar la línea de petición (método, path, protocolo)
            request_line = request.splitlines()[0]
            method, path, protocol = request_line.split()
            # Procesar headers (opcional)
            headers, body = self.process_response(request)
            if not headers:
                response = f"HTTP/1.1 400 Bad Request\n\nError al procesar la request"
                conn.sendall(response.encode())
            response, status_code = self.mainRouter.getResponse(method,path,headers,body)
            response = f"HTTP/1.1 {status_code} \n\n{response}"
            conn.sendall(response.encode())
            
        
        except Exception as e:
            logger.error(f"Error al manejar la conexión: {e}")
        finally:
            conn.close()
            
    def process_response(self,request):
        try:
            headers = {}
            lines = request.splitlines()
            for line in lines[1:]:
                if not line:
                    break  # Fin de los headers
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()
            
            body_start_index = lines.index("") + 1  # Índice de la primera línea del cuerpo
            body_lines = lines[body_start_index:]
            body = "\n".join(body_lines)
            return headers, body
        except Exception as e:
            logger.error(f"Error al procesar los headers: {e}")
            return False
        
        
