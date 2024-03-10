import json
import logging
import traceback
from types import TracebackType


def _format_exception(
    exc_type: type[Exception],
    exc_value: Exception,
    exc_traceback: TracebackType,
) -> str:
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    return "".join(lines)


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record_dict = {
            "timestamp": self.formatTime(record),
            "severity": record.levelname,
            "message": record.getMessage(),
            "module": record.name,
            "line": record.lineno,
        }
        if record.exc_info is not None:
            record_dict["traceback"] = _format_exception(*record.exc_info)
        return json.dumps(record_dict, indent=2)


def setup_logging(level: str) -> None:
    formatter = JsonFormatter()

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.handlers = [handler]
    root_logger.setLevel(level)
