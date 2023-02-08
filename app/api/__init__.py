"""logging initializer"""
import logging

level = logging.DEBUG
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(filename='api.log', level=level, format=fmt)
