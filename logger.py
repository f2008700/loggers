import logging

from colorama import Fore, Style


class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        timestamp = self.formatTime(record, datefmt="%H:%M:%S")
        log_message = super(ColoredFormatter, self).format(record)
        return f"{self.COLORS.get(record.levelname, '')} {timestamp} - {record.filename}:{record.lineno} - {record.levelname} - {record.getMessage()}{Style.RESET_ALL}"


class CustomLogger:
    def __init__(self, name, log_file=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = ColoredFormatter('%(asctime)s')

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Optionally, create a file handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


# Example usage:
if __name__ == "__main__":
    custom_logger = CustomLogger("my_logger", log_file="example.log")

    custom_logger.debug("Debug message")
    custom_logger.info("Info message")
    custom_logger.warning("Warning message")
    custom_logger.error("Error message")
    custom_logger.critical("Critical message")
