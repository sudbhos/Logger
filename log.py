import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter("%(asctime)s:%(message)s")
file_hander=logging.FileHandler("logs_details/logfile.log")
#file_hander.setLevel(Logging.ERROR)
file_hander.setFormatter(formatter)
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.addHandler(file_hander)

