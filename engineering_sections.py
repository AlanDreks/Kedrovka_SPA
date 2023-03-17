import sqlite3



# Функция добавления нового направления и оборудования в таблицу
def add_new_section():
    # Подключаемся к базе данных
    conn = sqlite3.connect('engineering_sections.db')
    cursor = conn.cursor()
    # Запрашиваем количество направлений
    num_directions = int(input("Введите количество направлений: "))
    # Добавляем каждое направление и оборудование в таблицу
    for i in range(num_directions):
        direction_name = input("Введите название направления: ")
        num_equipment = int(input(f"Введите количество оборудования в направлении {direction_name}: "))
        for j in range(num_equipment):
            equipment_name = input(f"Введите название оборудования {j + 1} в направлении {direction_name}: ")
            cursor.execute("INSERT INTO engineering_sections (direction, equipment) VALUES (?, ?);",
                             (direction_name, equipment_name))
    # Сохраняем изменения в базе данных
    conn.commit()
    print("Новые направления и оборудование успешно добавлены в таблицу!")
    # Закрываем соединение с базой данных
    conn.close()



def view_sections():
    # Подключаемся к базе данных
    conn = sqlite3.connect('engineering_sections.db')
    cursor = conn.cursor()

    # Получаем список всех направлений из таблицы
    cursor.execute("SELECT DISTINCT direction FROM engineering_sections")
    directions = cursor.fetchall()

    # Выводим список направлений
    print("\nСписок направлений:")
    for direction in directions:
        print(f"{direction[0]}")

    # Запрашиваем у пользователя выбор направления
    selected_direction = input("\nВведите название направления, для которого хотите посмотреть оборудование: ")

    # Получаем список оборудования для выбранного направления
    cursor.execute("SELECT equipment FROM engineering_sections WHERE direction = ?", (selected_direction,))
    equipment = cursor.fetchall()

    # Выводим список оборудования для выбранного направления
    print(f"\nСписок оборудования для направления {selected_direction}:")
    for eq in equipment:
        print(f"{eq[0]}")

    # Закрываем соединение с базой данных
    conn.close()


def delete_equipment():
    # Подключаемся к базе данных
    conn = sqlite3.connect('engineering_sections.db')
    cursor = conn.cursor()

    # Получаем список всех направлений из таблицы
    cursor.execute("SELECT DISTINCT direction FROM engineering_sections")
    directions = cursor.fetchall()

    # Выводим список направлений
    print("\nСписок направлений:")
    for direction in directions:
        print(f"{direction[0]}")

    # Запрашиваем у пользователя выбор направления
    selected_direction = input("\nВведите название направления, для которого хотите удалить оборудование: ")

    # Получаем список оборудования для выбранного направления
    try:
        cursor.execute("SELECT id, equipment FROM engineering_sections WHERE direction = ?", (selected_direction,))
        equipment = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving equipment: {e}")
        conn.close()
        return

    # Выводим список оборудования для выбранного направления
    if len(equipment) == 0:
        print(f"\nДля направления {selected_direction} не найдено оборудование!")
        conn.close()
        return
    else:
        print(f"\nСписок оборудования для направления {selected_direction}:")
        for eq in equipment:
            print(f"{eq[0]}: {eq[1]}")

    # Запрашиваем у пользователя выбор оборудования для удаления
    selected_equipment_id = int(input("\nВведите id оборудования, которое хотите удалить: "))

    # Удаляем выбранное оборудование
    try:
        cursor.execute("DELETE FROM engineering_sections WHERE id = ?", (selected_equipment_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while deleting equipment: {e}")
        conn.close()
        return

    print(f"\nОборудование с id {selected_equipment_id} успешно удалено из таблицы для направления {selected_direction}!")

    # Закрываем соединение с базой данных
    conn.close()


def list_sections():
    # Подключаемся к базе данных
    conn = sqlite3.connect('engineering_sections.db')
    cursor = conn.cursor()

    # Выбираем все направления из таблицы и выводим список
    cursor.execute("SELECT DISTINCT direction FROM engineering_sections")
    directions = cursor.fetchall()
    print("Список направлений:")
    for direction in directions:
        print(f"- {direction[0]}")

    # Выбираем направление и выводим список оборудования
    direction_name = input("\nВыберите направление, чтобы изменить оборудование: ")
    cursor.execute("SELECT equipment FROM engineering_sections WHERE direction = ?",
                   (direction_name,))
    equipment = cursor.fetchall()
    if len(equipment) > 0:
        print(f"Список оборудования в направлении {direction_name}:")
        for eq in equipment:
            print(f"- {eq[0]}")

        # Запрашиваем новое название оборудования и изменяем его в таблице
        old_name = input("\nВведите текущее название оборудования, которое нужно изменить: ")
        new_name = input("Введите новое название оборудования: ")
        cursor.execute("UPDATE engineering_sections SET equipment = ? WHERE direction = ? AND equipment = ?",
                       (new_name, direction_name, old_name))
        conn.commit()
        print(f"Название оборудования в направлении {direction_name} успешно изменено!")
    else:
        print(f"В направлении {direction_name} нет оборудования.")

    # Закрываем соединение с базой данных
    conn.close()


