from loguru import logger
from utils.utils_log import log_decorator
from utils.utils_timer import time_measure_decorator

# While infinito para ver funcionalidade do logger

#@log_decorator
#@time_measure_decorator
def contador():
    contador = 0
    while contador <=10000:
        logger.info(f"Contador: {contador}")
        print(contador)
        contador+=1

contador()