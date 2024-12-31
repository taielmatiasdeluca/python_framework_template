from ..logger import Logger

logger = Logger()


# Esta clase representa las cantidad de "caracteres, numeros, float, etc" para un campo.
class Length:
    length = 0
    max_length = 0

    def __init__(self, max_lenght=0):
        self.max_length = max_lenght

    def __eq__(self, value):
        # Permite obligar que el valor length, sea integrer.
        try:
            if value > self.max_length:
                logger.error(
                    f"Cantidad en un campo excede el maximo, se settea al maximo: {self.max_length}"
                )
                self.length = self.max_length
                return
            if value < 0:
                logger.error(
                    f"Cantidad en un campo debe ser mayor o igual a 0, se settea al minimo: 0"
                )
                self.length = 50
            self.length = int(value)

        except Exception as e:
            logger.error(e)
            logger.error("Error al comparar cantidad en un campo")
            self.length = 0

    def __int__(self):
        return int(self.edad)

    def __str__(self):
        return str(self.edad)


class Boolean:
    state = False

    def __eq__(self, value):
        # Permite obligar que el valor length, sea integrer.
        try:
            self.state = bool(value)
        except Exception as e:
            logger.error(e)
            logger.error("Error al errror, se esperaba un boolean")
            self.state = False

    def __get__(self, instance, owner):
        # Retorna la variable length al obtenerlo.
        return self.state
