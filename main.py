# from logging import getLogger, DEBUG, INFO, CRITICAL
from logging import getLogger
from lib1 import add, err, LogError

# # これはメインのファイルにのみ書く
# basicConfig(level=INFO)

# これはすべてのファイルに書く
logger = getLogger(__name__)

if __name__ == "__main__":
    
    from logging import basicConfig, StreamHandler, Formatter
    from logging.config import fileConfig
    # これはメインのファイルにのみ書く
    # basicConfig(level=DEBUG, format='%(asctime)s  %(name)-15s %(levelname)-8s %(message)s')
    # # logger.setLevel(INFO)
    # handler = StreamHandler()
    # formatter = Formatter('%(asctime)s  %(name)-15s %(levelname)-8s %(message)s')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)
    fileConfig(fname="./.logging.ini", disable_existing_loggers=False)


    logger.debug('debug')
    logger.info('info')

    result = add(1, 4)
    logger.info(f"result={result}")

    try:
        err()
    except LogError as e:
        logger.info(e)

    logger.info("CONPLETE!")
