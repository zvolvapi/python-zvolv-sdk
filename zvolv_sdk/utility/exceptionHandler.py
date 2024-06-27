import traceback
import requests
from ..modules.logger import Logger

class ExceptionHandler():
    _logger_instance = None

    @staticmethod
    def get_logger():
        if ExceptionHandler._logger_instance is None:
            ExceptionHandler._logger_instance = Logger.get_instance()
            ExceptionHandler._logger_instance.init(setLogLevel="ERROR")
        return ExceptionHandler._logger_instance

    @staticmethod
    def handle_generic_exception(error_msg):
        """
        Handles generic exceptions and logs the error message along with the traceback.

        :param error_msg: The error message to log
        :return: None
        """
        logger = ExceptionHandler.get_logger()
        logger.error(error_msg)
        logger.error(traceback.format_exc())
        raise Exception(error_msg)

    @staticmethod
    def handle_request_exception(exception, error_msg):
        """
        Handles specific exceptions and logs the error message along with the traceback.

        :param exception: The specific exception to handle
        :param error_msg: The error message to log
        :return: None
        """
        logger = ExceptionHandler.get_logger()
        if isinstance(exception, requests.exceptions.RequestException):
            response_msg = exception.response.text if exception.response else "No response received"
            logger.error(f"RequestException: {error_msg} - Response: {response_msg}")
            # logger.error(f"RequestException: {error_msg}")
        else:
            logger.error(f"Exception: {error_msg}")
        logger.error(traceback.format_exc())
        raise Exception(error_msg)