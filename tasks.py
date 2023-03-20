import sqlite3


def main():
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

    # Show a list of rooms for the selected floor and ask for the room number
    cursor.execute("SELECT * FROM rooms WHERE floor_id = ?", (floor_num,))
    rooms = cursor.fetchall()
    print('\nСписок помещений:\n')
    for r in rooms:
        print(f"{r[0]}. {r[2]}")
    room_num = int(input("\nВыберите номер помещения: "))

    # Connect to the engineering_sections database
    conn = sqlite3.connect('engineering_sections.db')
    cursor = conn.cursor()

    # Show a list of directions and ask the user for the direction name
    cursor.execute("SELECT DISTINCT direction FROM engineering_sections")
    directions = cursor.fetchall()
    print("Список направлений:")
    for d in directions:
        print(f"{d[0]}. {d[1]}")
    direction_name = input("\nВыберите направление, чтобы изменить оборудование: ")

    # Show a list of equipment for the selected direction
    cursor.execute("SELECT equipment FROM engineering_sections WHERE direction = ?",
                   (direction_name,))
    equipment = cursor.fetchall()
    if len(equipment) > 0:
        print(f"Список оборудования в направлении {direction_name}:")
        for e in equipment:
            print(f"{e[0]}. {e[2]}")

    # Ask the user for the equipment and count
    equipment_id = input("\nВведите текущее название оборудования, которое нужно изменить: ")
    count = int(input("Введите количество оборудования: "))

    # Connect to the actions database and show a list of actions
    conn = sqlite3.connect('actions.db')
    cursor = conn.execute("SELECT * FROM Actions")
    actions = cursor.fetchall()
    for action in actions:
        print(action[0], action[1])
    conn.close()

    # Ask the user for the action and get its id
    action_id = input("Введите id действия: ")

    # Write all data to the main database
    conn = sqlite3.connect('main_data.db')

    cursor.execute("INSERT INTO main_data (building_num, floor_num, room_num, direction_name, equipment_id, count, action_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
    (building_num, floor_num, room_num, direction_name, equipment_id, count, action_id))
    cursor.execute("SELECT * FROM main_data ORDER BY id DESC LIMIT 1")
    new_data = cursor.fetchone()
    print("\nДобавлено в базу данных:\n")
    print(f"ID: {new_data[0]}")
    print(f"Номер здания: {new_data[1]}")
    print(f"Номер этажа: {new_data[2]}")
    print(f"Номер помещения: {new_data[3]}")
    print(f"Направление: {new_data[4]}")
    print(f"Название оборудования: {new_data[5]}")
    print(f"Количество: {new_data[6]}")
    print(f"ID действия: {new_data[7]}")

    conn.commit()
    conn.close()

main()