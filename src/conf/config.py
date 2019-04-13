#! /usr/bin/env python

import logging
import os

def log():
    pass


class Config():
    """
    Basic config form flirone
    """

    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class DevConfig(Config):
    """
    Dev config
    """

    DEBUG = True


class ProConfig(Config):
    """
    pro config
    """
    DEBUG = False
