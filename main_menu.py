from bank_account import use_bank_account
from victory import play_victory
import file_manager


def show_menu():
    print()
    print('Консольный файловый менеджер')
    print()
    print('Меню:')
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')
    print()


def run_manager():

    account_balance = 0
    account_history = []

    while True:
        show_menu()
        choice = input('Выберите пункт меню: ')
        print()
        if choice == '1':
            print('Создать папку')
            file_manager.make_folder()
        elif choice == '2':
            print('Удалить (файл/папку)')
            file_manager.remove_file_or_folder()
        elif choice == '3':
            print('Копировать (файл/папку)')
            file_manager.copy_file_or_folder()
        elif choice == '4':
            print('Просмотр содержимого рабочей директории')
            file_manager.list_dir()
        elif choice == '5':
            print('Посмотреть только папки')
            file_manager.list_dir(show_folders=True, show_files=False)
        elif choice == '6':
            print('Посмотреть только файлы')
            file_manager.list_dir(show_folders=False, show_files=True)
        elif choice == '7':
            print('Просмотр информации об операционной системе')
            file_manager.show_platform_info()
        elif choice == '8':
            print('Создатель программы')
            file_manager.show_creator()
        elif choice == '9':
            print('Играть в викторину')
            play_victory()
        elif choice == '10':
            print('Мой банковский счет')
            use_bank_account(account_balance, account_history)
        elif choice == '11':
            print('Смена рабочей директории')
            file_manager.change_work_directory()
        elif choice == '12':
            print('Выход')
            break
        else:
            print('Неверный пункт меню')

        print()
        input('Для возврата в главное меню нажмите Enter')


run_manager()
