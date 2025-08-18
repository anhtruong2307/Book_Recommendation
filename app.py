from Book_Recommendation.exception.exception_handler import AppException
import sys
from Book_Recommendation.logger.log import logging

try:
    a = 3/0

except Exception as e:
    logging.infor()
    raise AppException(e,sys) from e