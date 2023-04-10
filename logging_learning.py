import logging


# logger = logging.getLogger()
# print(logger)
#
# def main(name):
#     logger.warning(f'Enter in the main() func: {name}')
#
# if __name__ == '__main__':
#     main('oleg')

# logging.basicConfig(level='DEBUG', filename='filename.log') #setting level to handler,\
# # handler working with filename.log
# logger = logging.getLogger()
# print(logger)
#
# logger.setLevel('DEBUG') #level of show attention (logging.DEBUG)
# print(logger.level)
#
# print(logger.handlers) # handlers
#
# def main(name):
#     logger.debug(f'Enter in the main() func: {name}')
#
# if __name__ == '__main__':
#     main('oleg')


# створюємо логер, даємо йому ім'я та встановлюємо рівень logging.DEBUG
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# створюємо handler для виведення в консоль та встановлюємо рівень DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# створюємо форматер: час виведення (asctime), ім'я модуля (name), рівень (levelname) та саме повідомлення (message)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# додаємо зазначений форматер до handler ch
ch.setFormatter(formatter)

# додаємо handler ch до логеру
logger.addHandler(ch)

# Створюємо файловий handler для логера:
fh = logging.FileHandler("app.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(formatter)

# додаємо файловий handler fh до логеру
logger.addHandler(fh)

# приклад виконання коду
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')