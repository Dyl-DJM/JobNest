from config.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Started the app")

    logger.info("Ended the app")


if __name__ == '__main__':
    main()
