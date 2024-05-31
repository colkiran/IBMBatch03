
import logging

logging.basicConfig(level=logging.DEBUG, filename="mylogs.log",
            format="%(asctime)s : %(levelname)s : %(message)s : %(filename)s : %(lineno)d")
inv = 1
num = 0

try:
    inv = 1 / num
except ZeroDivisionError as z:
    logging.critical(z)
except TypeError as t:
    logging.warning(t)
except Exception as e:
    logging.error(e)
else:
    logging.info(f"inverse of {num} is {inv}")
finally:
    print("Compelted diving a number.......")