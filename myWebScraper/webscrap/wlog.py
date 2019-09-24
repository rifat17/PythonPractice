import logging

def setCustomLogInfo(fileName):
    logging.basicConfig(filename=fileName,level=logging.INFO)

def report(e:Exception):
    logging.exception(str(e))
