from profil_logger.logger import ProfilLogger
from profil_logger.reader import ProfilLoggerReader
from profil_logger.handler.json_handler import JsonHandler
from datetime import datetime, timedelta

def test_reader_find_by_text(tmp_path):
    log_path = tmp_path / "logs.json"

    # create logger and write some test logs
    logger = ProfilLogger([JsonHandler(str(log_path))])
    logger.info("apple pie")
    logger.info("banana split")

    # now just use the reader to search logs
    reader = ProfilLoggerReader(JsonHandler(str(log_path)))
    result = reader.find_by_text("banana")

    assert len(result) == 1
    assert result[0].message == "banana split"

def test_reader_groupby_level(tmp_path):
    log_path = tmp_path / "logs.json"

    # log messages with multiple levels
    logger = ProfilLogger([JsonHandler(str(log_path))])
    logger.info("info message")
    logger.error("error message")
    logger.info("another info")

    reader = ProfilLoggerReader(JsonHandler(str(log_path)))
    grouped = reader.groupby_level()

    assert "INFO" in grouped
    assert "ERROR" in grouped
    assert len(grouped["INFO"]) == 2
    assert len(grouped["ERROR"]) == 1
