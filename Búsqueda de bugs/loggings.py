import logging

# INFO     = 10
# DEBUG    = 20
# WARNING  = 30
# ERROR    = 40
# CRITICAL = 50

logging.basicConfig(
    level=10
)

logging.info("mensage")
logging.debug("mensage")
logging.warning("mensage")
logging.error("mensage")
logging.critical("mensage")

# logging.basicConfig(  # Only take first config
#     level=10
# )

logging.info("mensage2")
logging.debug("mensage2")
logging.warning("mensage2")
logging.error("mensage2")
logging.critical("mensage2")
