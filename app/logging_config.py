import logging
import json
import sys


class JSONFormatter(logging.Formatter):
    """
    Formats log records as single-line JSON objects instead of
    plain text, so logs can be parsed, filtered, and queried by
    tools like Grafana Loki, Datadog, or even just jq on the CLI.
    """

    # Standard attributes every LogRecord has by default.
    # Anything NOT in this set was added via `extra=` and should
    # be included in the JSON output.
    _STANDARD_ATTRS = {
        "name",
        "msg",
        "args",
        "levelname",
        "levelno",
        "pathname",
        "filename",
        "module",
        "exc_info",
        "exc_text",
        "stack_info",
        "lineno",
        "funcName",
        "created",
        "msecs",
        "relativeCreated",
        "thread",
        "threadName",
        "processName",
        "process",
        "taskName",
    }

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }

        for key, value in record.__dict__.items():
            if key not in self._STANDARD_ATTRS:
                log_entry[key] = value

        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_entry)


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger("developer_toolkit_api")
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JSONFormatter())

    # Avoid duplicate handlers if setup_logging() is ever called more than once
    logger.handlers.clear()
    logger.addHandler(handler)

    return logger
