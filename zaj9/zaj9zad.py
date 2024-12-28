import datetime
import logging

import zaj9mod

logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(message)s")

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

try:
    zaj9mod.val_card_number("924803")
except ValueError as e:
    logger.error(e)

try:
    zaj9mod.val_card_number("1234567898765437")
except ValueError as e:
    logger.error(e)

try:
    zaj9mod.val_card_number("1234567891234564")
except ValueError as e:
    logger.error(e)

try:
    zaj9mod.val_card_number("1234567891234563")
except ValueError as e:
    logger.error(e)

try:
    zaj9mod.val_pesel("02070803628", datetime.date(1902, 7, 8), 0)
except ValueError as e:
    logger.error(e)

try:
    zaj9mod.val_pesel("02270803624", datetime.date(2002, 7, 8), 0)
except ValueError as e:
    logger.error(e)

try:
    zaj9mod.val_pesel("02270812350", datetime.date(2002, 7, 8), 1)
except ValueError as e:
    logger.error(e)

try:
    srednia_dni = zaj9mod.sr_wieku(1)
    print("Srednia wieku dni:", srednia_dni, "w przeliczeniu na lata:", srednia_dni / 365)
except ValueError as e:
    logger.error(e)
