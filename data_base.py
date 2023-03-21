import sqlite3


# База данных "Здания"
def create_buildings_table():
    conn = sqlite3.connect('buildings.db')
    cursor = conn.cursor()

    # Создаем таблицы для хранения информации о зданиях, этажах и помещениях
    cursor.execute("""CREATE TABLE IF NOT EXISTS buildings
                      (id INTEGER PRIMARY KEY,
                       name TEXT)
                   """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS floors
                      (id INTEGER PRIMARY KEY,
                       building_id INTEGER,
                       name TEXT,
                       FOREIGN KEY(building_id) REFERENCES buildings(id))
                   """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS rooms
                      (id INTEGER PRIMARY KEY,
                       floor_id INTEGER,
                       name TEXT,
                       FOREIGN KEY(floor_id) REFERENCES floors(id))
                   """)


# База данных "Сотрудники"
def create_employees_table():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS employees (
        last_name TEXT,
        first_name TEXT,
        middle_name TEXT,
        number TEXT,
        phone_number TEXT,
        position TEXT,
        login TEXT,
        password TEXT,
        rights TEXT
    )
    """

    cursor.execute(query)
    conn.commit()
    conn.close()


# База данных "Склад"
def create_warehouse_table():
    conn = sqlite3.connect('warehouse.db')
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS warehouse (
        equipment_name TEXT,
        count INTEGER,
        photo TEXT,
        price TEXT,
        sections TEXT,
        other INTEGER
    )
    """

    cursor.execute(query)
    conn.commit()
    conn.close()


# База данных "Действия"
def create_actions_table():
    conn = sqlite3.connect('actions.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS Actions
                 (id INTEGER PRIMARY KEY,
                 action_name TEXT NOT NULL);''')
    conn.close()


# База данных "Заявки"
def create_tasks_table():
    # Connect to the database
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    query = """CREATE TABLE IF NOT EXISTS tasks (
                       id INTEGER PRIMARY KEY,
                       building_id INTEGER,
                       building_name TEXT,
                       floor_id INTEGER,
                       floor_name TEXT,
                       room_id INTEGER,
                       room_name TEXT,
                       priority TEXT,
                       photo TEXT,
                       datetime DATETIME,
                       user_login TEXT,
                       status TEXT, 
                       worker TEXT
    )
    """
    cursor.execute(query)
    conn.commit()
    conn.close()

# Создание баз данных
def create_data_bases():
    create_buildings_table()
    create_employees_table()
    create_warehouse_table()
    create_actions_table()
    create_tasks_table()
