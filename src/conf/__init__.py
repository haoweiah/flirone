#!/usr/bin/env python
#! conding=utf:8
import os


def load_config():
    """
    load a config class
    :return:
    """
    mode = os.environ.get('MODE', 'DEV')

    try:
        if mode == 'PRO':
            from .config import ProConfig
            return ProConfig
        elif mode == 'DEV':
            from .config import DevConfig
            return DevConfig
        else:
            from .config import DevConfig
            return DevConfig

    except ImportError:
        from .config import Config
        return Config


CONFIG = load_config()