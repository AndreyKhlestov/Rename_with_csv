from logs.logs_setup import my_loggers


"""Loggers"""
logger = my_loggers['ProgramLogger']

"""Settings"""
setting_file = "settings.txt"

with open(setting_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# BASE_NAME_CSV_FILE = "eBay-OrdersReport-Jun-28-2023-01_39_23-0700-13106848719.csv"
# BASE_PATH = "C:/Users/Андрей/Desktop/переименование файлов/тесты/"
CSV_FILE_PATH = lines[0].split('=')[1].strip()
BASE_PATH = lines[1].split('=')[1].strip()
BASE_INCLUDE_REGEX = ".+_\d{6}_.+.eps$"
BASE_EXCLUDE_REGEX = "_\d{6}_\d{2}-\d{5}-\d{5}_"