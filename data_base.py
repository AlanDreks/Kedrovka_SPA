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
        position TEXT
    )
    """

    cursor.execute(query)
    conn.commit()
    conn.close()


# База данных "Направления"
def create_engineering_sections_table():
    conn = sqlite3.connect('engineering_sections.db')
    cursor = conn.cursor()

    # Создаем таблицу для хранения направлений и оборудования
    cursor.execute('''CREATE TABLE IF NOT EXISTS engineering_sections
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      direction TEXT NOT NULL,
                      equipment TEXT NOT NULL);''')

    # Закрываем соединение с базой данных
    conn.close()


# База данных "Действия"
def create_actions_table():
    conn = sqlite3.connect('actions.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS Actions
                 (id INTEGER PRIMARY KEY,
                 action_name TEXT NOT NULL);''')
    conn.close()

# База данных "Склад"
# База данных "Отчет по месяцам"
# База данных "Отчет за год"


# Создание баз данных
def create_data_bases():
    create_buildings_table()
    create_employees_table()
    create_engineering_sections_table()
    create_actions_table()