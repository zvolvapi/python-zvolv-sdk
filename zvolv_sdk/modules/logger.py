import logging

class Logger:
    def __init__(self, logLevel="INFO"):
        self.logger = logging.getLogger(__name__)
        log_level = getattr(logging, logLevel.upper(), logging.INFO)
        self.logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # Create a handler to log messages to the console
        console_handler = logging.StreamHandler()
        # Add the formatter to the handler
        console_handler.setFormatter(formatter)
        # Add the handler to the logger
        self.logger.addHandler(console_handler)

    def info(self, message):
        """
        :param message: Message to log
        :return: None
        """
        self.logger.info(message)

    def error(self, message):
        """
        :param message: Message to log
        :return: None
        """
        self.logger.error(message)

    def debug(self, message):
        """
        :param message: Message to log
        :return: None
        """
        self.logger.debug(message)

    def warning(self, message):
        """
        :param message: Message to log
        :return: None
        """
        self.logger.warning(message)
    
    def exception(self, message):
        """
        :param message: Message to log
        :return: None
        """
        self.logger.exception(message)