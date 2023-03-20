from building import new_buildings, display_rooms, update_building_name, change_floor_name, change_room_name, \
    add_floor, add_rooms, delete_floor, delete_room
from employees import add_employee, show_employees, change_employees, delete_employee
from engineering_sections import add_new_section, view_sections, delete_equipment, list_sections
from actions import view_actions, add_action, delete_action
from data_base import create_data_bases

# Создание всех баз данных
create_data_bases()


def building_main():
    while True:
        action_building = int(input('\n\nДобавить новое здание и всю информацию по нему - 1'
                                    '\nПросмотр здания и его этажей - 2'
                                    '\nИзменение названия здания - 3'
                                    '\nИзменение названия этажа - 4'
                                    '\nИзменение названия помещения - 5'
                                    '\nДобавление нового этажа - 6'
                                    '\nДобавления нового помещения - 7'
                                    '\nУдаление этажа - 8'
                                    '\nУдаление помещения - 9'
                                    '\nНазад - 10'
                                    '\n\nВыберите действие, которое хотите выполнить: '))
        if action_building == 1:
            # Функция добавления информации о здании
            new_buildings()
        elif action_building == 2:
            # Call the display_rooms() function to start the program
            display_rooms()
        elif action_building == 3:
            # Изменение названия здания
            update_building_name()
        elif action_building == 4:
            # Изменение названия этажа
            change_floor_name()
        elif action_building == 5:
            # Изменение названия помещения
            change_room_name()
        elif action_building == 6:
            # Добавление нового этажа
            add_floor()
        elif action_building == 7:
            # Функция для добавления нового помещения
            add_rooms()
        elif action_building == 8:
            # Удаление этажа
            delete_floor()
        elif action_building == 9:
            # Функция для удаления помещения
            delete_room()
        elif action_building == 10:
            # Назад
            main_function()
        elif action_building == 78:
            print('\nПрограмма завершена')
            exit()
        else:
            print('Ошибка! Попробуйте еще раз!')


def employees_main():
    while True:
        action_employees = int(input('\n\nДобавление нового сотрудника - 1'
                                     '\nПоказать всю информацию по сотрудникам - 2'
                                     '\nИзменить один из параметров сотрудника - 3'
                                     '\nУдалить сотрудника - 4'
                                     '\nНазад - 5'
                                     '\n\nВыберите действие, которое хотите выполнить: '))
        if action_employees == 1:
            # Добавление нового сотрудника
            add_employee()
        elif action_employees == 2:
            # Показать всю информацию по сотрудникам
            show_employees()
        elif action_employees == 3:
            # Изменить параметр сотрудника
            change_employees()
        elif action_employees == 4:
            # Удалить сотрудника
            delete_employee()
        elif action_employees == 5:
            # Назад
            main_function()
        elif action_employees == 78:
            print('\nПрограмма завершена')
            exit()
        else:
            print('Ошибка! Попробуйте еще раз!')


def engineering_sections_main():
    while True:
        action_engineering_sections = int(input('\n\nДобавить новое оборудования - 1'
                                                '\nПосмотреть список оборудования - 2'
                                                '\nУдалить оборудование - 3'
                                                '\nИзменить название оборудования - 4'
                                                '\nНазад - 5'
                                                '\n\nВыберите действие, которое хотите выполнить: '))
        if action_engineering_sections == 1:
            # Добавление нового оборудования
            add_new_section()
        elif action_engineering_sections == 2:
            # Показываем список направлений и оборудования
            view_sections()
        elif action_engineering_sections == 3:
            # удаляем оборудование
            delete_equipment()
        elif action_engineering_sections == 4:
            # изменяем оборудование
            list_sections()
        elif action_engineering_sections == 5:
            # Назад
            main_function()
        elif action_engineering_sections == 78:
            print('\nПрограмма завершена')
            exit()
        else:
            print('Ошибка! Попробуйте еще раз!')


def actions_main():
    while True:
        print('\nВыберите действие: ')
        action_actions = int(input('\n\nДобавление нового действия - 1'
                                   '\nПоказать всю информацию по действиям - 2'
                                   '\nУдалить действие - 3'
                                   '\nНазад - 4'
                                   '\n\nВыберите действие, которое хотите выполнить: '))
        if action_actions == 1:
            # Добавление нового действия
            add_action()
        elif action_actions == 2:
            # Показать список действий
            view_actions()
        elif action_actions == 3:
            # Удалить дейтсиве
            delete_action()
        elif action_actions == 4:
            # Назад
            main_function()
        elif action_actions == 78:
            print('\nПрограмма завершена')
            exit()
        else:
            print('Ошибка! Попробуйте еще раз!')


def main_function():
    while True:
        print()

        action_main_py = int(input('\nЗдания - 1'
                                   '\nСотрудники - 2'
                                   '\nНаправления инженерии - 3'
                                   '\nДействия - 4'
                                   '\n\nВыберите действие, которое хотите выполнить: '))
        if action_main_py == 1:
            # Здания
            building_main()
        elif action_main_py == 2:
            # Сотрудники
            employees_main()
        elif action_main_py == 3:
            # Направления инженерии
            engineering_sections_main()
        elif action_main_py == 4:
            # Действия
            actions_main()
        elif action_main_py == 78:
            print('\nПрограмма завершена')
            exit()
        else:
            print('Ошибка! Попробуйте еще раз!')


main_function()
