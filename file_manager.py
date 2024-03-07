import os
import platform
import shutil


def make_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        return f"Папка '{folder_name}' успешно создана."
    except OSError as error:
        return f"Ошибка при создании папки: {error}"


def remove_file_or_folder(object_name):
    if not os.path.exists(object_name):
        return "Файл или папка не найдены."

    if os.path.isfile(object_name):
        # Удаляем файл
        os.remove(object_name)
        return f"Файл '{object_name}' был удален."
    elif os.path.isdir(object_name):
        # Удаляем папку
        shutil.rmtree(object_name)
        return f"Папка '{object_name}' была удалена."


def copy_file_or_folder(source, destination):

    if not os.path.exists(source):
        return f'Не найдено файла или папки с названием {source}'

    if os.path.isfile(source):
        try:
            shutil.copy(source, destination)
            return f"Файл '{source}' скопирован в '{destination}'"
        except IOError as error:
            return f"Не удалось скопировать файл. Ошибка: {error}"
    elif os.path.isdir(source):
        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
            return f"Папка '{source}' скопирована в '{destination}'"
        except shutil.Error as error:
            return f"Не удалось скопировать папку. {error}"
    else:
        return f'{source} не является папкой или файлом'


def list_dir(show_folders=True, show_files=True):
    contents = os.listdir()
    objets_list = []
    for item in contents:
        if show_folders and os.path.isdir(item):
            objets_list.append(item)
        if show_files and os.path.isfile(item):
            objets_list.append(item)
    return objets_list


def show_creator():
    return 'Alexander Melikhov'


def show_platform_info():
    info_list = []

    platform_info = platform.platform()
    info_list.append(f"Платформа: {platform_info}")

    architecture = platform.architecture()
    info_list.append(f"Архитектура: {architecture}")

    processor_info = platform.processor()
    info_list.append(f"Процессор: {processor_info}")

    return info_list


def change_work_directory(new_directory):
    try:
        os.chdir(new_directory)
        return f"Текущая рабочая директория изменена на: {os.getcwd()}"
    except Exception as e:
        return f"Ошибка при смене директории: {e}"
