import logging 

log_path = input("Enter your log document path : ")
x = int(input("Enter a number(x) : "))

# logging using basic config funcion

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(message)s')

logging.debug(f'the value of x is {x} - debug level.')
logging.info('this message for info level.')
logging.warning('this message occur warning level.')

try:
    1/x
except Exception:
    logging.error('value of x is zero for error level.')

logging.critical('the critical level called')

#logging using logger, formatter, handler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s - %(message)s')

file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


logger.info('this message is received')
logger.warning('warning!!!')
logger.critical('critical!!!!!')
