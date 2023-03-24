import sqlite3


def add_employee():
    # открываем соединение с базой данных
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    # запрашиваем данные нового сотрудника у пользователя
    last_name = input("\nВведите фамилию сотрудника: ")
    first_name = input("Введите имя сотрудника: ")
    middle_name = input("Введите отчество сотрудника: ")
    number = input("Введите номер сотрудника: ")
    phone_number = input("Введите номер телефона сотрудника: ")
    position = input("Введите должность сотрудника: ")
    login = input("Введите логин сотрудника: ")
    password = input("Введите пароль сотрудника: ")
    print('Вы можете выбрать следующие права:\nadmin\nworker\nemployee of another department')
    rights = input("Введите права сотрудника: ")

    # формируем запрос на добавление нового сотрудника
    query = """INSERT INTO employees (last_name, first_name, middle_name, number, phone_number, position, login, password, rights)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    # используем параметризованный запрос для безопасного добавления данных
    cursor.execute(query, (last_name, first_name, middle_name, number, phone_number, position, login, password, rights))

    # сохраняем изменения в базе данных
    conn.commit()

    # закрываем соединение
    conn.close()


def show_employees():
    # открываем соединение с базой данных
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    # формируем запрос на извлечение всех записей из таблицы employees
    query = """SELECT * FROM employees"""

    # выполняем запрос и получаем результат
    cursor.execute(query)
    employees = cursor.fetchall()

    # выводим информацию по каждому сотруднику
    print()
    for employee in employees:
        print(f"Фамилия: {employee[0]}\n"
              f"Имя: {employee[1]}\n"
              f"Отчество: {employee[2]}\n"
              f"Номер: {employee[3]}\n"
              f"Номер телефона: {employee[4]}\n"
              f"Должность: {employee[5]}\n"
              f"Логин: {employee[6]}\n"
              f"Пароль: {employee[7]}\n"
              f"Права: {employee[8]}")
        print()

    # закрываем соединение
    conn.close()


def change_employees():
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
        print(f"{employee[0]}. {employee[1]} {employee[2]} {employee[3]} ({employee[4]}) - {employee[5]}, {employee[6]}")

    # запрашиваем у пользователя номер сотрудника, информацию которого нужно изменить
    employee_id = input("\nВведите номер сотрудника, информацию которого нужно изменить: ")
    employee_id = int(employee_id)

    # выполняем запрос на выборку сотрудника с указанным номером
    query = "SELECT last_name, first_name, middle_name, number, phone_number, position, login, password, rights FROM employees WHERE rowid = ?"
    cursor.execute(query, (employee_id,))
    employee = cursor.fetchone()

    # выводим информацию о сотруднике
    print(f"\nИнформация о сотруднике:")
    print(f"Фамилия: {employee[0]}")
    print(f"Имя: {employee[1]}")
    print(f"Отчество: {employee[2]}")
    print(f"Номер: {employee[3]}")
    print(f"Номер телефона: {employee[4]}")
    print(f"Должность: {employee[5]}")
    print(f"Логин: {employee[6]}")
    print(f"Пароль: {employee[7]}")
    print(f"Права: {employee[8]}")

    # запрашиваем у пользователя параметр, который нужно изменить
    field_name = input("Введите название параметра, который нужно изменить (last_name, "
                       "first_name, middle_name, number, phone_number, position, login, password, rights): ")

    # проверяем, что пользователь ввел допустимое название параметра
    allowed_field_names = ["last_name", "first_name", "middle_name", "number", "phone_number", "position", "login",
                           "password", "rights"]
    while field_name not in allowed_field_names:
        field_name = input("Введите корректное название параметра: ")
    field_value = input("Введите новое значение параметра: ")

    # выполняем запрос на обновление информации о сотруднике
    query = f"UPDATE employees SET {field_name} = ? WHERE rowid = ?"
    cursor.execute(query, (field_value, employee_id))
    conn.commit()

    # закрываем соединение
    conn.close()


def delete_employee():
    # открываем соединение с базой данных
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    # выполняем запрос на получение всех сотрудников
    cursor.execute("SELECT * FROM employees")

    # выводим всех сотрудников
    print("\nСписок сотрудников:")
    for row in cursor.fetchall():
        print(row[0], row[1], row[2], row[3])

    # запрашиваем данные сотрудника, которого нужно удалить
    last_name = input("\nВведите фамилию сотрудника, которого нужно удалить: ")
    first_name = input("Введите имя сотрудника, которого нужно удалить: ")
    middle_name = input("Введите отчество сотрудника, которого нужно удалить: ")

    # формируем запрос на удаление сотрудника и всех его параметров
    query = """DELETE FROM employees 
               WHERE last_name=? AND first_name=? AND middle_name=?"""

    # используем параметризованный запрос для безопасного удаления данных
    cursor.execute(query, (last_name, first_name, middle_name))

    # сохраняем изменения в базе данных
    conn.commit()

    # закрываем соединение
    conn.close()


def change_password():
    # открываем соединение с базой данных
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    # запрашиваем логин и пароль у пользователя
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    # формируем запрос на поиск пользователя в базе данных
    query = """SELECT * FROM employees WHERE login = ? AND password = ?"""
    cursor.execute(query, (login, password))

    # извлекаем данные о пользователе из запроса
    user = cursor.fetchone()

    if user is not None:
        # если пользователь найден, выводим его данные
        print(f'Добро пожаловать, {user[1]} {user[0]}!')
        # предлагаем пользователю сменить пароль
        change_password = input('Желаете сменить пароль? (да/нет): ')
        if change_password.lower() == 'да':
            new_password = input('Введите новый пароль: ')
            # формируем запрос на обновление пароля в базе данных
            update_query = """UPDATE employees SET password = ? WHERE login = ?"""
            cursor.execute(update_query, (new_password, login))
            conn.commit()
            print('Пароль успешно изменен!')
    else:
        print('Пользователь не найден.')

    # закрываем соединение с базой данных
    conn.close()
