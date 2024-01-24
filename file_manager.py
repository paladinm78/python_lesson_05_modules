import os
import platform
import shutil
from victory import confirmation


def make_folder():
    folder_name = input('Укажите имя папки: ')
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Папка '{folder_name}' успешно создана.")
    except OSError as error:
        print(f"Ошибка при создании папки: {error}")


def remove_file_or_folder():
    object_name = input('Укажите имя файла или папки: ')

    if os.path.exists(object_name):
        if os.path.isfile(object_name):
            # Удаляем файл
            os.remove(object_name)
            print(f"Файл '{object_name}' был удален.")
        elif os.path.isdir(object_name):
            # Удаляем папку
            shutil.rmtree(object_name)
            print(f"Папка '{object_name}' была удалена.")
    else:
        print("Файл или папка не найдены.")


def copy_file_or_folder():
    source = input('Укажите имя файла или папки для копирования: ')
    if not os.path.exists(source):
        print(f'Не найдено файла или папки с названием {source}')
        return

    destination = input('Укажите путь, куда будем копировать: ')
    if os.path.exists(destination):
        if not confirmation(f'{destination} уже существует. Перезаписать? (да/нет): '):
            print('Отмена копирования')
            return

    if os.path.isfile(source):
        try:
            shutil.copy(source, destination)
            print(f"Файл '{source}' скопирован в '{destination}'")
        except IOError as error:
            print(f"Не удалось скопировать файл. Ошибка: {error}")
    elif os.path.isdir(source):
        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
            print(f"Папка '{source}' скопирована в '{destination}'")
        except shutil.Error as error:
            print(f"Не удалось скопировать папку. {error}")
    else:
        print(f'{source} не является папкой или файлом')


def list_dir(show_folders=True, show_files=True):
    contents = os.listdir()
    for item in contents:
        if show_folders and os.path.isdir(item):
            print(item)
        if show_files and os.path.isfile(item):
            print(item)


def show_creator():
    print('Alexander Melikhov')


def show_platform_info():

    platform_info = platform.platform()
    print(f"Платформа: {platform_info}")

    architecture = platform.architecture()
    print(f"Архитектура: {architecture}")

    processor_info = platform.processor()
    print(f"Процессор: {processor_info}")


def change_work_directory():
    new_directory = input('Укажите путь к новой рабочей директории: ')
    try:
        os.chdir(new_directory)
        print(f"Текущая рабочая директория изменена на: {os.getcwd()}")
    except Exception as e:
        print(f"Ошибка при смене директории: {e}")
