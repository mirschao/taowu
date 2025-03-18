# -*- coding: utf-8 -*-


from sanic.log import LOGGING_CONFIG_DEFAULTS


LOGGING_CONFIG_DEFAULTS['formatters']['generic']['class'] = 'sanic.logging.formatter.ProdFormatter'
LOGGING_CONFIG_DEFAULTS['formatters']['access']['class'] = 'sanic.logging.formatter.ProdAccessFormatter'


class MyConfig:
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 3364
    SECRET = "k8YtZq7Xn2r5u7x!A%D*G-JaNdRgUjWnZr4u7w!z%C*F"
    LOGGING_CONFIG_DEFAULTS = LOGGING_CONFIG_DEFAULTS
