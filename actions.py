import sqlite3

def view_actions():
    conn = sqlite3.connect('actions.db')
    cursor = conn.execute("SELECT * FROM Actions")
    actions = cursor.fetchall()
    for action in actions:
        print(action[0], action[1])
    conn.close()

def add_action():
    conn = sqlite3.connect('actions.db')
    action_name = input("Введите новое действие: ")
    conn.execute("INSERT INTO Actions (action_name) VALUES (?)", (action_name,))
    conn.commit()
    conn.close()

def delete_action():
    conn = sqlite3.connect('actions.db')
    action = input("Введите действие, которого нужно удалить: ")
    conn.execute("DELETE FROM Actions WHERE action_id=?", (action,))
    conn.commit()
    conn.close()