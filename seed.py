import faker
import random
import sqlite3

NUMBER_OF_USERS = 40
NUMBER_OF_TASKS = 30

database = './database.db'

def generate_data(users_number,tasks_number, start_index, end_index):
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()
    for _ in range(users_number):
        fake_users.append((fake_data.name(), fake_data.unique.email(),))

    for _ in range(tasks_number):
        status_id = random.randint(1,3)
        user_id = random.randint(start_index,end_index)
        fake_tasks.append((fake_data.sentence(), fake_data.text(),status_id,user_id,))

    return fake_users, fake_tasks



def insert_data_to_db(users,tasks):
    with sqlite3.connect(database) as con:
        con.execute("PRAGMA foreign_keys = ON")
        cur = con.cursor()

        sql_insert_users = 'INSERT INTO users(fullname,email) VALUES (?,?)'
        cur.executemany(sql_insert_users, users)

        sql_insert_tasks = 'INSERT INTO tasks(title,description,status_id,user_id) VALUES (?,?,?,?)'
        cur.executemany(sql_insert_tasks, tasks)

        con.commit()


if __name__ == '__main__':

    with sqlite3.connect(database) as con:
        cur = con.cursor()
        sql = sql_get_ids = """ SELECT MAX(id) FROM users"""
        cur.execute(sql_get_ids)
        result = cur.fetchone()[0]
        max_id = result if result is not None else 0

    # Future IDs of newly inserted users
    start_index = max_id + 1
    end_index = max_id + NUMBER_OF_USERS

    users,tasks = generate_data(NUMBER_OF_USERS,NUMBER_OF_TASKS,start_index,end_index)
    # print(users)
    # print(tasks)
    insert_data_to_db(users,tasks)



