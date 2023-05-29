import os
import sqlite3
from contextlib import closing

# creating path to database
db_filepath = os.path.join(os.path.dirname(__file__), 'database')
db_file = os.path.join(db_filepath, 'users.db')
if not os.path.exists(db_file):
    os.mkdir(db_filepath)
print('\nPath: ', db_file)

with closing(sqlite3.connect(db_file)) as conn:
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS sign_up_database(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT NOT NULL,
                     email TEXT NOT NULL,
                     password TEXT NOT NULL,
                     created_date TEXT NOT NULL
                 )""")

# with closing(sqlite3.connect(db_file)) as conn:
#     conn.execute("""""")
# print('\nTable created successfully')

# updating datable
# with closing(sqlite3.connect(db_file)) as connection:
#     # connection.execute("""
#     #                    ALTER TABLE sign_up_database ADD COLUMN creation_date TEXT NOT NULL
#     #                    """)

#     row = connection.execute("""
#                              SELECT * FROM sign_up_database
#                              """).rowcount
#     print(row, connection.total_changes)

# print('successfully update!')


def add_record(name, email, password, date):
    with closing(sqlite3.connect(db_file, check_same_thread=False)) as conn:
        conn.execute(
            """INSERT INTO sign_up_database (username, email,password,created_date) 
            VALUES (?,?,?,?)""",
            (name, email, password, date))
        conn.commit()


# def add_name(name):
#     with closing(sqlite3.connect(db_file)) as conn:
#         conn.execute(
#             "INSERT INTO sign_up_database (username) VALUES (?)", (name))
#         conn.commit()


# def add_email(email):
#     with closing(sqlite3.connect(db_file)) as conn:
#         conn.execute("INSERT INTO customers (email) VALUES (?)", (email))
#         conn.commit()


# def add_password(password):
#     with closing(sqlite3.connect(db_file)) as conn:
#         conn.execute("INSERT INTO customers (password) VALUES (?)", (password))
#         conn.commit()


# def add_date(date):
#     with closing(sqlite3.connect(db_file)) as conn:
#         conn.execute("INSERT INTO customers (date) VALUES (?)", (date))
#         conn.commit()

def show_all():
    with closing(sqlite3.connect(db_file)) as conn:
        records = conn.execute("SELECT * FROM sign_up_database").fetchall()
        for i in records:
            print(i)
        conn.commit()


if __name__ == '__main__':
    # record = ['Prince Kyeremeh', 'prince@gmail.com', 'hello123', 'May-25-2023']
    # record = ['Macayla Frempah', 'macayla@gmail.com', '1234thy', 'May-24-2023']
    #   , s2, s3, s4 = record
    # add_record(*record)
    print('successfully added')
    show_all()


# with closing(sqlite3.connect(db_file)) as conn:
#     conn.execute("SELECT rowid, * FROM sqlite_master")
#     print(conn.total_changes)
#     # conn.commit()

# with closing(sqlite3.connect(db_file)) as conn:
#     conn.execute("DROP TABLE sign_up_database")
#     conn.commit()
# print('successfully deleted')
