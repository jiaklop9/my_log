#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARNING)
sh = logging.StreamHandler()

fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(message)s"
formatter = logging.Formatter(fmt)
sh.setFormatter(formatter)
logger.addHandler(sh)

logger.debug("debug")
logger.info("info")
logger.warning("warn")
logger.error("error")
logger.critical("critical")


if __name__ == '__main__':
    pass
