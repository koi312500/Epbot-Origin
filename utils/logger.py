"""
    <logger.py>
    로깅 유틸
"""

from datetime import datetime
import os
import traceback
from constants import Constants

import config


def err(error):
    """
    오류 기록을 남길 때 사용해요!
    """
    try:
        raise error
    except Exception:
        error_message = traceback.format_exc()
        log(f"[오류] {error_message}", "err", True)
        return error_message


def warn(message: str):
    """
    경고 기록을 남길 때 사용해요!
    """
    log(f"[경고] {message}", "warn")


def info(message: str):
    """
    일반적인 기록을 남길 때 사용해요!
    """
    log(f"[정보] {message}", "info")


def debug(message: str):
    """
    디버그 모드를 켰을 때만 기록해 줘요!
    """
    if config.debug:
        log(f"[디버그] {message}", "debug")


def query(message: str):
    """쿼리 로그 옵션이 켜져 있을 때만 기록해 줘요!"""
    if config.query_logging:
        log(f"[쿼리] {message}", "query")


def log(message: str, level: str, iserror=False):
    now = datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    log_msg = f"{time} / {message}"
    log_msg_colored = f"\033[1;36m{time}\033[0m /{Constants.LOGGER_COLORS[level]} {message}\033[0m"
    print(log_msg_colored)
    save(log_msg)
    if iserror:
        save_error(log_msg)


def save(message):
    if not (os.path.isdir("logs")):
        os.makedirs(os.path.join("logs"))
    now = datetime.now()
    time_text = now.strftime("%Y-%m-%d")
    if not os.path.isfile("logs/log_" + time_text + ".txt"):
        f = open("logs/log_" + time_text + ".txt", "w", encoding="utf-8")
    else:
        f = open("logs/log_" + time_text + ".txt", "a", encoding="utf-8")
    f.write(message + "\n")
    f.close()


def save_error(message):
    now = datetime.now()
    time_text = now.strftime("%Y-%m-%d")
    if not os.path.isfile("logs/error_log_" + time_text + ".txt"):
        f = open("logs/error_log_" + time_text + ".txt", "w", encoding="utf-8")
    else:
        f = open("logs/error_log_" + time_text + ".txt", "a", encoding="utf-8")
    f.write(message + "\n")
    f.close()
