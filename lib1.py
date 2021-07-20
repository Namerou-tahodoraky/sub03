from logging import getLogger, DEBUG, INFO, CRITICAL

# これはすべてのファイルに書く
logger = getLogger(__name__)

def add(a, b):
    logger.info(f"{a}, {b}")
    return a + b

class LogError(Exception):
    def __str__(self):
        return "LogError発生!"

def err():
    raise LogError()

if __name__ == "__main__":
    from logging import basicConfig, StreamHandler, Formatter
    # これはメインのファイルにのみ書く
    basicConfig(level=CRITICAL)
