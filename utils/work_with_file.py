import os
from re import Pattern

from config import BASE_PATH, BASE_EXCLUDE_REGEX, BASE_INCLUDE_REGEX, logger, INFO
from objects import File


def search_files(directory: str = BASE_PATH,
                 include_regex: Pattern = BASE_INCLUDE_REGEX,  # регулярное выражение для поиска файлов
                 exclude_regex: Pattern = BASE_EXCLUDE_REGEX  # регулярное выражение для исключения файлов
                 ) -> list:
    """Поиск файлов в указанной директории при помощи регулярных выражений"""
    result = list()
    if not (os.path.exists(directory) and os.path.isdir(directory)):
        INFO.add_error("Не найден указанная директория для поиска файлов для переименование. "
                       "Проверьте корректность указанного пути.")
        return result

    for root, dirs, files in os.walk(directory):
        for file in files:
            # если файл соответствует регулярному выражению для поиска, но не соответствует для исключения.
            if include_regex.search(file) and not exclude_regex.search(file):
                result.append(File(root, file))
    return result


def rename_file(old_name: str, new_name: str, directory: str):
    """Переименование файла"""
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    try:
        os.rename(old_path, new_path)
        logger.debug(f"Файл {old_name} успешно переименован в {new_name} в директории {directory}")
        INFO.add_rename_file(new_name)
    except FileNotFoundError:
        text_error = f"Файл не найден - {old_path}."
        logger.__error(text_error)
        INFO.add_error(text_error)
    except PermissionError:
        text_error = f"Нет разрешения на переименование файла - {old_path}."
        logger.__error(text_error)
        INFO.add_error(text_error)
    except FileExistsError:
        text_error = f"Файл с таким именем уже существует - {old_path}."
        logger.__error(text_error)
        INFO.add_error(text_error)
    except Exception as e:
        logger.__error(f"Произошла системная ошибка при переименовании.\n"
                       f"Ошибка: {e}\n"
                       f"Файл: {old_path}")
        INFO.add_error(f"Произошла системная ошибка при переименовании файла {old_name}")
