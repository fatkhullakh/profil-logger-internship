from profil_logger.logger import ProfilLogger
from profil_logger.handler.json_handler import JsonHandler
import os

def test_logger_creates_json_file(tmp_path):
    # create a test file in a temporary directory
    log_path = tmp_path / "test.json"

    # use our logger with JSON handler
    logger = ProfilLogger([JsonHandler(str(log_path))])

    # log two messages
    logger.info("Test info message")
    logger.error("Test error")

    # file should exist and contain both messages
    assert log_path.exists()
    with open(log_path) as f:
        content = f.read()
        assert "Test info message" in content
        assert "Test error" in content
