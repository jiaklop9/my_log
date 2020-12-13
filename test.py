#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
from main import Logger

logyyx = Logger('test', logging.DEBUG, logging.WARNING)


if __name__ == '__main__':

    logyyx.info('一个info信息')
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warning('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.critical('一个致命critical信息')
