import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="D5.log", 
                    filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")

logging.info("THIS IS A INFO")
logging.debug("THIS IS A DEBUG VALUE")
logging.warning("THIS IS A WARNIG")
logging.error("THIS IS A ERROR")
logging.critical("THIS IS CRITICAL")