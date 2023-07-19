import re

from logs.logs_setup import my_loggers
from objects import Info


"""Loggers"""
logger = my_loggers['ProgramLogger']

"""Settings"""
setting_file = "settings.txt"

with open(setting_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()


CSV_FILE_PATH = lines[0].split('=')[1].strip()
BASE_PATH = lines[1].split('=')[1].strip()
BASE_INCLUDE_REGEX = re.compile(".+_\d{6}_.+.(eps|png)$")
BASE_EXCLUDE_REGEX = re.compile("_\d{6}_\d{2}-\d{5}-\d{5}_")
INFO = Info()
