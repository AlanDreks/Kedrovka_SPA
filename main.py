from building import new_buildings, display_rooms, update_building_name, change_floor_name, change_room_name, add_floor, add_rooms, delete_floor, delete_room
from employees import add_employee, show_employees, change_employees, delete_employee
from engineering_sections import add_new_section, view_sections, delete_equipment, list_sections
from actions import view_actions, add_action, delete_action









def building_main():
    while True:
        print('\n\nВыберите действие, которое хотите выполнить:\n')
        action = int(input('Добавить новое здание и всю информацию по нему - 1\n'
                           'Просмотр здания и его этажей - 2\n'
                           'Изменение названия здания - 3\n'
                           'Изменение названия этажа - 4\n'
                           'Изменение названия помещения - 5\n'
                           'Добавление нового этажа - 6\n'
                           'Добавления нового помещения - 7\n'
                           'Удаление этажа - 8\n'
                           'Удаление помещения - 9\n\n'))
        if action == 1:
            #Функция добавления информации о здании
            new_buildings()
        elif action == 2:
            # Call the display_rooms() function to start the program
            display_rooms()
        elif action == 3:
            #Изменение названия здания
            update_building_name()
        elif action == 4:
            #Изменение названия этажа
            change_floor_name()
        elif action == 5:
            #Изменение названия помещения
            change_room_name()
        elif action == 6:
            #Добавление нового этажа
            add_floor()
        elif action == 7:
            #Функция для добавления нового помещения
            add_rooms()
        elif action == 8:
            #Удаление этажа
            delete_floor()
        elif action == 9:
            #Функция для удаления помещения
            delete_room()
        elif action == 78:
            print('\nПрограмма завершена')
            break


def employees_main():
    while True:
        print('\nВыберите действие: ')

        action = int(input('\nДобавление нового сотрудника - 1\n'
                           '\nПоказать всю информацию по сотрудникам - 2\n'
                           '\nИзменить один из параметров сотрудника - 3\n'
                           '\nУдалить сотрудника - 4\n\n'))
        if action == 1:
            #Добавление нового сотрудника
            add_employee()
        elif action == 2:
            #Показать всю информацию по сотрудникам
            show_employees()
        elif action == 3:
            #Изменить параметр сотрудника
            change_employees()
        elif action == 4:
            #Удалить сотрудника
            delete_employee()


        elif action == 78:
            print('Программа завершена')
            break



def engineering_sections_main():
    while True:
        print('\nВыберите действие: ')

        action = int(input('\nДобавить новое оборудования - 1\n'
                           '\nПосмотреть список оборудования - 2\n'
                           '\nУдалить оборудование - 3\n'
                           '\nИзменить название оборудования - 4\n\n'))
        if action == 1:
            #Добавление нового оборудования
            add_new_section()
        elif action == 2:
            #Показываем список направлений и оборудования
            view_sections()
        elif action == 3:
            #удаляем оборудование
            delete_equipment()
        elif action == 4:
            #изменяем оборудование
            list_sections()


        elif action == 78:
            print('Программа завершена')
            break


def actions_main():
    while True:
        print('\nВыберите действие: ')

        action = int(input('\nДобавление нового действия - 1\n'
                           '\nПоказать всю информацию по действиям - 2\n'
                           '\nУдалить действие - 43\n\n'))
        if action == 1:
            #Добавление нового сотрудника
            add_action()
        elif action == 2:
            #Показать всю информацию по сотрудникам
            view_actions()
        elif action == 3:
            #Изменить параметр сотрудника
            change_employees()
        elif action == 4:
            #Удалить сотрудника
            delete_action()
        elif action == 78:
            print('Программа завершена')
            break



while True:
    print('\nВыберите действие: ')

    action = int(input('\nЗдания - 1\n'
                       '\nСотрудники - 2\n'
                       '\nНаправления инженерии - 3\n'
                       '\nДействия - 4\n\n'))
    if action == 1:
        #Здания
        building_main()
    elif action == 2:
        #Сотрудники
        employees_main()
    elif action == 3:
        #Направления инженерии
        engineering_sections_main()
    elif action == 4:
        #Действия
        actions_main()
    elif action == 78:
        print('Программа завершена')
        break



