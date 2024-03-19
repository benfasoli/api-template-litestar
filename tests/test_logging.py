import json
import logging
from unittest import mock

from pytest import CaptureFixture

from src.logging import setup_logging


def test_message_formatted_as_json(capsys: CaptureFixture[str]) -> None:
    setup_logging("DEBUG")

    logger = logging.getLogger(__name__)
    logger.info("message content")

    stdout, stderr = capsys.readouterr()
    assert stdout == ""

    expected_record = {
        "time": mock.ANY,
        "severity": "INFO",
        "message": "message content",
        "module": "tests.test_logging",
        "line": 14,
    }
    record = json.loads(stderr)
    assert record == expected_record
