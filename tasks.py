import sqlite3
from datetime import datetime


def submit_task(user_login):
    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()

    # Retrieve list of buildings from database
    cursor.execute("SELECT id, name FROM buildings")
    buildings = cursor.fetchall()

    # Display list of buildings and prompt user to select one
    print("Выберите здание:")
    for building in buildings:
        print(f"{building[0]}. {building[1]}")
    building_id = input("Номер здания: ")

    # Retrieve name of selected building
    cursor.execute("SELECT name FROM buildings WHERE id = ?", (building_id,))
    building_name = cursor.fetchone()[0]

    # Retrieve list of floors for selected building
    cursor.execute("SELECT id, name FROM floors WHERE building_id = ?", (building_id,))
    floors = cursor.fetchall()

    # Display list of floors and prompt user to select one
    print("Выберите этаж:")
    for floor in floors:
        print(f"{floor[0]}. {floor[1]}")
    floor_id = input("Номер этажа: ")

    # Retrieve name of selected floor
    cursor.execute("SELECT name FROM floors WHERE id = ?", (floor_id,))
    floor_name = cursor.fetchone()[0]

    # Retrieve list of rooms for selected floor
    cursor.execute("SELECT id, name FROM rooms WHERE floor_id = ?", (floor_id,))
    rooms = cursor.fetchall()

    # Display list of rooms and prompt user to select one
    print("Выберите помещение:")
    for room in rooms:
        print(f"{room[0]}. {room[1]}")
    room_id = input("Номер помещения: ")

    # Retrieve name of selected room
    cursor.execute("SELECT name FROM rooms WHERE id = ?", (room_id,))
    room_name = cursor.fetchone()[0]

    # Prompt user to select priority
    priority = input("Приоритет (высокий/низкий): ")

    # Prompt user to attach photo
    photo = input("Прикрепить фото (да/нет): ")

    # Prompt user to confirm and submit request
    confirm = input("Подтвердить заявку (да/нет): ")
    if confirm.lower() == 'да':
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        # Insert new task into tasks table with current datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO tasks (building_id, building_name, floor_id, floor_name, room_id, room_name, "
                       "priority, photo, datetime, user_login) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (building_id, building_name, floor_id, floor_name, room_id, room_name, priority, photo, now, user_login))
        conn.commit()
        print("Заявка отправлена!")
    else:
        print("Отменено.")

    # Closing the connection to the database
    cursor.close()
    conn.close()

# viewing submitted applications
def view_tasks():
    # Connect to the database
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Retrieve list of tasks from database
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    # Display list of tasks
    for task in tasks:
        print(f"Номер заявки: {task[0]}")
        print(f"Здание: {task[2]} ({task[1]})")
        print(f"Этаж: {task[4]} ({task[3]})")
        print(f"Помещение: {task[6]} ({task[5]})")
        print(f"Приоритет: {task[7]}")
        print(f"Фото: {task[8]}")
        print(f"Дата и время: {task[9]}")
        print(f"Пользователь: {task[10]}")
        print("\n")

    # Closing the connection to the database
    cursor.close()
    conn.close()

    # tommorow
    # date
    # status
