from loguru import logger
from sys import stderr

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time}|{level}|{message}|{file}",
    level="INFO"
)

logger.debug("Um aviso para o dev no futuro")
logger.info("Informação importante do processo")
logger.warning("Um aviso que algo vai parar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu um erro que vai abortar a aplicação")