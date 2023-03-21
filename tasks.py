import sqlite3
from datetime import datetime


def submit_task(user_login_task):
    # открываем соединение с базой данных
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    # выполняем запрос на выборку всех сотрудников
    query = "SELECT rowid, last_name, first_name, middle_name, number, phone_number, position, login, password, rights FROM employees"
    cursor.execute(query)
    employees = cursor.fetchall()

    # выводим список всех сотрудников
    print("\nСписок всех сотрудников:\n")
    for employee in employees:
        print(f"{employee[0]}. {employee[1]} {employee[2]}")

    # запрашиваем у пользователя номер сотрудника, информацию которого нужно изменить
    employee_id = input("\nВведите номер сотрудника: ")
    employee_id = int(employee_id)
    cursor.execute("SELECT last_name, first_name  FROM employees WHERE rowid = ?", (employee_id,))
    worker_name = cursor.fetchone()
    worker = f'{worker_name[0]} {worker_name[1]}'

    # закрываем соединение с базой данных
    cursor.close()
    conn.close()




    # Connect to the database
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()

    # Retrieve list of buildings from database
    cursor.execute("SELECT id, name FROM buildings")
    buildings = cursor.fetchall()

    # Display list of buildings and prompt user to select one
    print("\nВыберите здание:")
    for building in buildings:
        print(f"{building[0]}. {building[1]}")
    building_id = input("\nНомер здания: ")

    # Retrieve name of selected building
    cursor.execute("SELECT name FROM buildings WHERE id = ?", (building_id,))
    building_name = cursor.fetchone()[0]

    # Retrieve list of floors for selected building
    cursor.execute("SELECT id, name FROM floors WHERE building_id = ?", (building_id,))
    floors = cursor.fetchall()

    # Display list of floors and prompt user to select one
    print("\nВыберите этаж:")
    for floor in floors:
        print(f"{floor[0]}. {floor[1]}")
    floor_id = input("\nНомер этажа: ")

    # Retrieve name of selected floor
    cursor.execute("SELECT name FROM floors WHERE id = ?", (floor_id,))
    floor_name = cursor.fetchone()[0]

    # Retrieve list of rooms for selected floor
    cursor.execute("SELECT id, name FROM rooms WHERE floor_id = ?", (floor_id,))
    rooms = cursor.fetchall()

    # Display list of rooms and prompt user to select one
    print("\nВыберите помещение:")
    for room in rooms:
        print(f"{room[0]}. {room[1]}")
    room_id = input("\nНомер помещения: ")

    # Retrieve name of selected room
    cursor.execute("SELECT name FROM rooms WHERE id = ?", (room_id,))
    room_name = cursor.fetchone()[0]

    # Prompt user to select priority
    priority = input("\nПриоритет (высокий/низкий): ")

    # Prompt user to attach photo
    photo = input("\nПрикрепить фото (да/нет): ")

    # Prompt user to confirm and submit request
    confirm = input("\nПодтвердить заявку (да/нет): ")
    if confirm.lower() == 'да':
        user_login = user_login_task
        status = 'новая'
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        # Insert new task into tasks table with current datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO tasks (building_id, building_name, floor_id, floor_name, room_id, room_name, "
                       "priority, photo, datetime, user_login, status, worker) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (building_id, building_name, floor_id, floor_name, room_id, room_name, priority, photo, now,
                         user_login, status, worker))
        conn.commit()
        cursor.close()
        conn.close()
        print("\nЗаявка отправлена!")
    else:
        print("\nОтменено. Можно попробовать еще раз!")
        submit_task(user_login_task)


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
        print(f"\n\nНомер заявки: {task[0]}")
        print(f"Локализация: {task[2]}, {task[4]}, {task[6]} ")
        print(f"Приоритет: {task[7]}")
        print(f"Фото: {task[8]}")
        print(f"Дата и время: {task[9]}")
        print(f"Заказчик: {task[10]}")
        print(f"Статус: {task[11]}")
        print(f"Исполнитель: {task[12]}")
        print("\n")

    # Closing the connection to the database
    cursor.close()
    conn.close()

    # tommorow
    # date
    # status
