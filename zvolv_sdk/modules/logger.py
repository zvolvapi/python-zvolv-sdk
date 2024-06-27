import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, session=None, base_url=None):
        self.session = session
        self.base_url = base_url
        self.logger = None
        self.activityLogger = None

    def init(self, activityLogger=None, setLogLevel="INFO"):
        """
        Initializes the logger with the specified activity logger and log level.

        :param activityLogger (object): The activity logger(Kafka) instance to be used for logging.
        :param setLogLevel (str): The logging level to be set. Valid values are "INFO", "ERROR", "DEBUG" and "WARNING".
        :return: None
        """
        self.activityLogger = activityLogger
        if setLogLevel not in {"INFO", "ERROR", "DEBUG", "WARNING"}:
            raise ValueError("Valid setLofLevel values are 'INFO', 'ERROR', 'DEBUG' and 'WARNING'.")

        if not self.activityLogger:
            # Create a logger and Formatting Log Messages
            self.logger = logging.getLogger(__name__)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            # Create a handler to log messages to the console
            console_handler = logging.StreamHandler()
            # Add the formatter to the handler
            console_handler.setFormatter(formatter)
            # Add the handler to the logger
            self.logger.addHandler(console_handler)
            # Set log level
            log_level = getattr(logging, setLogLevel.upper(), logging.INFO)
            self.logger.setLevel(log_level)
            # self.logger.setLevel(logging.ERROR)
        else:
            pass

    @staticmethod
    def get_instance(session=None, base_url=None):
        return Logger(session, base_url)

    def info(self, message):
        """
        :param message: Message to log
        :return: None
        """
        if not self.logger:
            self.logger = Logger()
            self.logger.init()
        self.logger.info(message)

    def error(self, message):
        """
        :param message: Message to log
        :return: None
        """
        if not self.logger:
            self.logger = Logger()
            self.logger.init()
        self.logger.error(message)

    def debug(self, message):
        """
        :param message: Message to log
        :return: None
        """
        if not self.logger:
            self.logger = Logger()
            self.logger.init()
        self.logger.debug(message)

    def warning(self, message):
        """
        :param message: Message to log
        :return: None
        """
        if not self.logger:
            self.logger = Logger()
            self.logger.init()
        self.logger.warning(message)

















    # def init(self):
    #     if False:
    #         pass
    #     else:
    #         # Create a logger
    #         self.logger = logging.getLogger(__name__)
    #         # Formatting Log Messages
    #         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    #
    #         # # To log messages to a file
    #         # # file_handler = logging.FileHandler('app.log')
    #         # rotating_handler = RotatingFileHandler('app.log', maxBytes=3000000, backupCount=3)
    #         # self.logger.addHandler(rotating_handler)
    #         # rotating_handler.setFormatter(formatter)
    #
    #         # To log messages to the console
    #         console_handler = logging.StreamHandler()
    #         self.logger.addHandler(console_handler)
    #         console_handler.setFormatter(formatter)

    # # To log messages to a file
    # # file_handler = logging.FileHandler('app.log')
    # rotating_handler = RotatingFileHandler('app.log', maxBytes=3000000, backupCount=3)
    # self.logger.addHandler(rotating_handler)
    # rotating_handler.setFormatter(formatter)