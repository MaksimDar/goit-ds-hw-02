import sqlite3

database = './database.db'

def execute_query(database, sql):
    with sqlite3.connect(database) as con:
        con.execute("PRAGMA foreign_keys = ON")
        cur = con.cursor()
        cur.execute(sql)
        con.commit() 
        return cur.fetchall()

# Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
sql_cmd_first = """ SELECT * FROM tasks WHERE user_id = 2;"""


# Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
sql_cmd_second = """ SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = "new");"""

# Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
sql_cmd_third = """UPDATE tasks SET status_id = (SELECT id FROM status where name="in progress") WHERE id = 17;"""

# Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
sql_cmd_fourth = """SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks );"""

# Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
sql_cmd_fifth = """INSERT INTO tasks (title,description,status_id,user_id) VALUES ("Do tennis practise today", "Tennis is a professional sport. Grand Slams are 4 main tournaments ", (SELECT id FROM status WHERE name="new"), 17);"""


# Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'. Priority to new tasks, then to in progress
sql_cmd_sixth = """SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status where name IN("new","in progress")) ORDER BY status_id;"""

# Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
sql_cmd_seventh = """DELETE FROM tasks where id = 5; """

# Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
sql_cmd_eightth = """SELECT * FROM users WHERE email LIKE '%example.com'; """

# Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
sql_cmd_ninth = """UPDATE users SET fullname = 'Maksym Dovhusha' WHERE id = 19;"""

# Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
sql_cmd_tenth = """SELECT (SELECT name FROM status WHERE status.id = tasks.status_id) AS name_of_status, COUNT(status_id) AS number_of_new_tasks FROM tasks GROUP BY status_id;"""

# Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
sql_cmd_eleventh = """SELECT u.email,t.title,t.description, t.status_id FROM users AS u JOIN tasks AS t ON t.user_id = u.id WHERE u.email LIKE '%example.com';"""

# Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
sql_cmd_twelfth = """SELECT id AS task_id, title FROM tasks WHERE description IS NULL OR description = '';"""

# Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
sql_cmd_thirteenth = """SELECT u.fullname, u.email, t.title, t.description,t.status_id FROM users AS u JOIN tasks AS t ON t.user_id = u.id AND t.status_id = (SELECT id FROM status WHERE name = 'in progress');"""

# Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
sql_cmd_fourteenth = """SELECT u.fullname, u.email, COUNT(t.user_id) AS total_tasks FROM users AS u LEFT JOIN tasks AS t ON t.user_id = u.id GROUP BY u.id, u.fullname, u.email ORDER BY total_tasks DESC;"""

if __name__ == '__main__':
    # Execute sql commands
    sql_cmd_first, sql_cmd_second, sql_cmd_third, sql_cmd_fourth,sql_cmd_fifth, sql_cmd_sixth, sql_cmd_seventh,sql_cmd_eightth,sql_cmd_ninth,sql_cmd_tenth,sql_cmd_eleventh,sql_cmd_twelfth,sql_cmd_thirteenth, sql_cmd_fourteenth
   
    print(execute_query(database,sql_cmd_eightth))




