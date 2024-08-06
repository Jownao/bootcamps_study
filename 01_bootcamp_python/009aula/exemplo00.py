from loguru import logger
from utils.utils_log import log_decorator

# Configurando o arquivo de log com rotação de 5MB
logger.add("meu_app.log", rotation="5 MB")

@log_decorator
def soma(x,y):
    print(x)
    print(y)
    print(x+y)
    return x+y

soma(2,3)

