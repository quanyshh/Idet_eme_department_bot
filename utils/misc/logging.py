import logging

logging.basicConfig(
    handlers=[logging.FileHandler(filename="log_file.log", encoding='utf-8', mode='a+')],
    format=u'[LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(filename)s  %(message)s',
    level=logging.INFO,
    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
)
