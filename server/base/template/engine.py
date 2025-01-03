import re
from ..logger import Logger

logger = Logger()


class TemplateEngine:
    html = ''
    template_path = ''
    
    
    
    
    def __init__(self, template_path):
        # TODO: implementar un descriptor sobre template path para que soo pueda ser una string.
        self.template_path = template_path
        self.html = self._get_custom_template()
        
    def _get_custom_template(self):
        """
        Obtiene el template html y lo ingresa en la variable html.
        """
        if not self.template_path:
            return ''
        if not self.template_path.endswith('.html'):
            logger.error(f"El template {self.template_path} no es un archivo .html")
            return ''
        try:
            html = open(self.template_path).read()
            return html
        except Exception as e:
            logger.error(e)
            logger.error(f"Error al abrir el template {self.template_path}")
            return ''
    
    def setVariable(self,variable,value,cant=False):
        """
        Modifica el template html, reemplazando la variable con el valor.
        """
        patron = rf"{{\s*{variable}\s*}}"
        self.html =  re.sub(patron, value, self.html, count=cant)
        
    def render(self):
        """
        Devuelve el template html.
        """
        return self.html
        
        
        
        
    
        
    
    
    