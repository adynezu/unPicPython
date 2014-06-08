import logging


logging.basicConfig(level=logging.DEBUG)

def safeExecution(my_func):
    try:
        my_func()
    except Exception as e:
        logging.exception("Good... You got an error!")

@safeExecution
def testFunction():
    1 / 0
