import time
import logging

logger = logging.getLogger(__name__)


class RequestLoggerMiddleware:
    """
    Middleware personalizado que registra información de cada petición:
    - Ruta
    - Método HTTP
    - Usuario autenticado
    - Tiempo de ejecución
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Registrar tiempo de inicio
        start_time = time.time()
        
        # Procesar la petición
        response = self.get_response(request)
        
        # Calcular tiempo de ejecución
        execution_time = (time.time() - start_time) * 1000  # en milisegundos
        
        # Obtener información del usuario
        user = request.user.username if request.user.is_authenticated else "Anonymous"
        
        # Registrar en consola
        log_message = f"[{request.method}] {request.path} - User: {user} - Time: {execution_time:.2f}ms"
        logger.info(log_message)
        print(log_message)  # También imprimir en consola
        
        return response
