import os


BASE_PATH = "C:/Users/Андрей/Desktop/переименование файлов/тесты/"


def rename_file(old_name, new_name, directory=BASE_PATH):

    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    os.rename(old_path, new_path)
    print(f"Переименовал файл {old_name} в {new_name}")


# Укажите текущее имя файла и новое имя файла
current_name_file = "test.txt"
new_name_file = "test_1.txt"

rename_file(current_name_file, new_name_file)



path = os.listdir(BASE_PATH)
for i_path in path:
    print(i_path)


