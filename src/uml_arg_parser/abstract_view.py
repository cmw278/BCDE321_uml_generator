from abc import ABC, abstractmethod
import logging


class AbstractView (ABC):
    @abstractmethod
    def show(self, msg: str) -> str:
        """Show a message to the user.
        """
        pass

    @abstractmethod
    def get_input(self, msg: str = None):
        """Get input frmo the user.
        """
        pass

    _log_levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    def __init__(self, prog: str):
        self.set_logger(prog)
        self.set_log_handler()
        self.set_log_formatter()

    def set_logger(self, prog: str) -> None:
        logger = logging.getLogger(prog)
        logger.setLevel(logging.DEBUG)
        self._logger = logger

    def set_log_handler(self) -> None:
        self._log_handler = logging.StreamHandler()
        self.set_log_level('INFO')
        self._logger.addHandler(self._log_handler)

    def set_log_level(self, level: str) -> None:
        assert level in self._log_levels.keys()
        self._log_handler.setLevel(self._log_levels[level])

    def set_log_formatter(self) -> None:
        formatter = logging.Formatter('%(name)s :: [%(levelname)s]'
                                      ' -> %(message)s')
        self._log_handler.setFormatter(formatter)

    def debug(self, *args: any, **kwargs: any) -> None:
        self._logger.debug(*args, **kwargs)

    def info(self, *args: any, **kwargs: any) -> None:
        self._logger.info(*args, **kwargs)

    def warning(self, *args: any, **kwargs: any) -> None:
        self._logger.warning(*args, **kwargs)

    def error(self, *args: any, **kwargs: any) -> None:
        self._logger.error(*args, **kwargs)

    def critical(self, *args: any, **kwargs: any) -> None:
        self._logger.critical(*args, **kwargs)
