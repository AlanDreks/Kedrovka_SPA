import sqlite3


#Добавление нового помещения 1
conn = sqlite3.connect('buildings.db')
cursor = conn.cursor()

def new_buildings():
    num_buildings = int(input("Сколько зданий вы хотите добавить? "))
    for b in range(num_buildings):
        # Запрашиваем данные у пользователя
        building_name = input(f"\nВведите название здания {b + 1}: ")
        num_floors = int(input("\nВведите количество этажей: "))

        # Добавляем информацию о здании в таблицу buildings
        cursor.execute("INSERT INTO buildings (name) VALUES (?)", (building_name,))
        building_id = cursor.lastrowid

        # Запрашиваем и добавляем информацию об этажах и помещениях
        for i in range(num_floors):
            floor_name = input(f"\nВведите название {i + 1}-го этажа: ")
            num_rooms = int(input(f"\nВведите количество помещений на {i + 1}-м этаже: "))

            # Добавляем информацию об этаже в таблицу floors
            cursor.execute("INSERT INTO floors (building_id, name) VALUES (?, ?)", (building_id, floor_name))
            floor_id = cursor.lastrowid

            # Добавляем информацию о помещениях в таблицу rooms
            for j in range(num_rooms):
                room_name = input(f"\nВведите название {j + 1}-го помещения на {floor_name}: ")
                cursor.execute("INSERT INTO rooms (floor_id, name) VALUES (?, ?)", (floor_id, room_name))

        #Сохраняем базу данных
        conn.commit()
    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()



#Показ всех зданий, этажей, помещений 2
def display_rooms():
    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()

    # Show a list of buildings and ask the user for the building number
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    print('\nСписок зданий: \n')
    for b in buildings:
        print(f"{b[0]}. {b[1]}")
    building_num = int(input("\nВыберите номер здания: "))

    # Show all floors for the selected building and ask for the floor number
    cursor.execute("SELECT * FROM floors WHERE building_id = ?", (building_num,))
    floors = cursor.fetchall()
    print('\nСписок этажей: \n')
    for f in floors:
        print(f"{f[0]}. {f[2]}")
    floor_num = int(input("\nВыберите номер этажа: "))

    # Show a list of rooms for the selected floor
    cursor.execute("SELECT * FROM rooms WHERE floor_id = ?", (floor_num,))
    rooms = cursor.fetchall()
    print('\nСписок помещений:\n')
    for r in rooms:
        print(r[2])

    # Close the database connection
    cursor.close()
    conn.close()


#Функция для изменения названия здания 3
def update_building_name():
    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()

    # Show a list of buildings and ask the user for the building number
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    print('\nСписок зданий: \n')
    for b in buildings:
        print(f"{b[0]}. {b[1]}")
    building_id = int(input("\nВведите номер здания, которое вы хотите изменить: "))
    new_building_name = input("\nВведите новое название здания: ")

    cursor.execute("UPDATE buildings SET name = ? WHERE id = ?", (new_building_name, building_id))
    conn.commit()

    print("\nНазвание здания обновлено успешно!")


#Функция для изменения названия этажа 4
def change_floor_name():
    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()
    # Show a list of buildings and ask the user for the building number
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    print('\nСписок зданий: \n')
    for b in buildings:
        print(f"{b[0]}. {b[1]}")
    building_num = int(input("\nВведите номер здания: "))
    # Show all floors for the selected building and ask for the floor number
    cursor.execute("SELECT * FROM floors WHERE building_id = ?", (building_num,))
    floors = cursor.fetchall()
    print('\nСписок этажей: \n')
    for f in floors:
        print(f"{f[0]}. {f[2]}")
    floor_num = int(input("\nВведите номер этажа: "))
    new_floor_name = input("\nВведите новое название этажа: ")

    # Обновляем информацию об этаже в таблице floors
    cursor.execute("UPDATE floors SET name = ? WHERE building_id = ? AND id = ?", (new_floor_name, building_num, floor_num))

    # Сохраняем базу данных
    conn.commit()
    print('Сохранили базу данных')

    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()
    print('Закрыли соединение с базой данных')


#Функция для изменения названия помещения 5
def change_room_name():
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()

    # Get a list of buildings
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    if not buildings:
        print("No buildings found.")
        return

    # Ask the user for the building number
    print("\nСписок зданий:\n")
    for i, building in enumerate(buildings):
        print(f"{i+1}. {building[1]}")
    building_num = int(input("\nВведите номер здания: "))
    building_id = buildings[building_num-1][0]

    # Get a list of floors in this building
    cursor.execute("SELECT * FROM floors WHERE building_id = ?", (building_id,))
    floors = cursor.fetchall()
    if not floors:
        print("No floors found in this building.")
        return

    # Ask the user for the floor number
    print("\nСписок этажей:\n")
    for i, floor in enumerate(floors):
        print(f"{i+1}. {floor[2]}")
    floor_num = int(input("\nВведите номер этажа: "))
    floor_id = floors[floor_num-1][0]

    # Get a list of rooms on this floor
    cursor.execute("SELECT * FROM rooms WHERE floor_id = ?", (floor_id,))
    rooms = cursor.fetchall()
    if not rooms:
        print("No rooms found on this floor.")
        return

    # Ask the user for the room number and new name
    print("\nСписок помещений:\n")
    for i, room in enumerate(rooms):
        print(f"{i+1}. {room[2]}")
    room_num = int(input("\nВведите номер помещения: "))
    new_name = input("Введите новое название помещения: ")
    room_id = rooms[room_num-1][0]

    # Update the room name in the database
    cursor.execute("UPDATE rooms SET name = ? WHERE id = ?", (new_name, room_id))
    conn.commit()

    print("\nПомещение успешно переименованно.")


#Функция для добавления нового этажа и помещений на нем 6
def add_floor():
    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()

    # Show a list of buildings and ask the user for the building number
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    print('\nСписок зданий: \n')
    for b in buildings:
        print(f"{b[0]}. {b[1]}")
    building_id = int(input("\nВведите номер здания: \n"))

    # Запрос списка этажей
    cursor.execute("SELECT id, name FROM floors WHERE building_id=?", (building_id,))
    floors = cursor.fetchall()

    # Выводим список этажей
    print("Список этажей:\n")
    for floor in floors:
        print(f"{floor[0]}. {floor[1]}")

    # Запрос названия нового этажа
    new_floor_name = input("\nВведите название нового этажа: ")

    # Добавляем информацию об этаже в таблицу floors
    cursor.execute("INSERT INTO floors (building_id, name) VALUES (?, ?)", (building_id, new_floor_name))
    floor_id = cursor.lastrowid

    # Запрос количества помещений на новом этаже
    num_rooms = int(input("\nВведите количество помещений на новом этаже: "))

    # Добавляем информацию о помещениях в таблицу rooms
    for j in range(num_rooms):
        room_name = input(f"\nВведите название {j + 1}-го помещения на {new_floor_name}: ")
        cursor.execute("INSERT INTO rooms (floor_id, name) VALUES (?, ?)", (floor_id, room_name))

    # Сохраняем базу данных
    conn.commit()
    print("Информация успешно добавлена в базу данных.")


#Функция для добавления нового помещения 7
def add_rooms():
    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()

    # Show a list of buildings and ask the user for the building number
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    print('\nСписок зданий: \n')
    for b in buildings:
        print(f"{b[0]}. {b[1]}")
    building_id = int(input("\nВведите номер здания: \n"))

    # Show all floors for the selected building and ask for the floor number
    cursor.execute("SELECT * FROM floors WHERE building_id = ?", (building_id,))
    floors = cursor.fetchall()
    print('\nСписок этажей: \n')
    for f in floors:
        print(f"{f[0]}. {f[2]}")
    floor_id = int(input("\nВыберите номер этажа: "))

    # Show a list of rooms for the selected floor
    cursor.execute("SELECT * FROM rooms WHERE floor_id = ?", (floor_id,))
    rooms = cursor.fetchall()
    print('\nСписок помещений:\n')
    for r in rooms:
        print(r[2])
    # Ask the user how many rooms they want to add to this floor
    num_rooms = int(input("\nВведите количество комнат для добавления: "))
    # Ask for the names of each room and add them to this floor
    for i in range(num_rooms):
        room_name = input(f"\nВведите название {i + 1}-й комнаты: ")
        cursor.execute("INSERT INTO rooms (floor_id, name) VALUES (?, ?)", (floor_id, room_name))

    # Save the changes to the database
    conn.commit()
    print("Изменения сохранены")


#Функция для удаления этажа 8
def delete_floor():
    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()
    # Show a list of buildings and ask the user for the building number
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    print('\nСписок зданий: \n')
    for b in buildings:
        print(f"{b[0]}. {b[1]}")
    building_num = int(input("\nВведите номер здания: "))
    # Show all floors for the selected building and ask for the floor number
    cursor.execute("SELECT * FROM floors WHERE building_id = ?", (building_num,))
    floors = cursor.fetchall()
    print('\nСписок этажей: \n')
    for f in floors:
        print(f"{f[0]}. {f[2]}")
    floor_id = int(input("\nВведите номер этажа: "))
    # Находим все помещения на заданном этаже
    cursor.execute("SELECT id FROM rooms WHERE floor_id=?", (floor_id,))
    room_ids = cursor.fetchall()
    # Удаляем каждое помещение на заданном этаже
    for room_id in room_ids:
        cursor.execute("DELETE FROM rooms WHERE id=?", (room_id[0],))
    # Удаляем этаж
    cursor.execute("DELETE FROM floors WHERE id=?", (floor_id,))
    conn.commit()
    conn.close()


#Функция для удаления помещения 9
def delete_room():
    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()
    # Show a list of buildings and ask the user for the building number
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    print('\nСписок зданий: \n')
    for b in buildings:
        print(f"{b[0]}. {b[1]}")
    building_num = int(input("\nВведите номер здания: "))
    # Show all floors for the selected building and ask for the floor number
    cursor.execute("SELECT * FROM floors WHERE building_id = ?", (building_num,))
    floors = cursor.fetchall()
    print('\nСписок этажей: \n')
    for f in floors:
        print(f"{f[0]}. {f[2]}")
    floor_id = int(input("\nВведите номер этажа: "))
    # Удаляем помещение
    cursor.execute("SELECT * FROM rooms WHERE floor_id = ?", (floor_id,))
    rooms = cursor.fetchall()
    print("\nСписок помещений:\n")
    for room in rooms:
        print(f"{room[0]}. {room[2]}")
    room_id = input('\nВведите номер удаляемого помещения: ')
    cursor.execute("DELETE FROM rooms WHERE id=?", (room_id,))
    conn.commit()
    conn.close()



