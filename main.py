#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, path, console_level=logging.DEBUG, file_level=logging.WARNING):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(console_level)
        # 设置文件日志
        # fh = logging.FileHandler(path)
        # 按文件大小分割日志: 满3切割，最多保留10个日志文件
        fh = RotatingFileHandler(path, maxBytes=3 * 1024, backupCount=10)
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message, *args, **kwargs):
        self.logger.error(message, *args, **kwargs)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logyyx = Logger('main', logging.ERROR, logging.WARNING)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warning('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.critical('一个致命critical信息')
