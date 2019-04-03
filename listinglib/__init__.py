# coding=utf-8
import errno
import logging
import logging.config
import logging.handlers
import os

__author__ = 'TienHN'


def mkdir_p(path):
    """http://stackoverflow.com/a/600612/190597 (tzot)"""
    try:
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

class MakeFileHandler(logging.handlers.RotatingFileHandler):
    def __init__(self, filename):
        mkdir_p(os.path.dirname(filename))
        logging.handlers.RotatingFileHandler.__init__(self, filename=filename, maxBytes=500)

listing_lib_logger = logging.getLogger("Listing lib")
listing_lib_logger.setLevel(logging.INFO)
f_handler = MakeFileHandler('var/log/listing_lib/listing_lib.log')
f_handler.setLevel(logging.INFO)
f_format = logging.Formatter('%(levelname)-5.5s %(asctime)s [%(name)s][%(module)s:%(lineno)d] [%(pathname)s] %(message)s')
f_handler.setFormatter(f_format)
listing_lib_logger.addHandler(f_handler)

