import sqlite3
from database.queries import create_table, insert_order, select_orders

path_db = "database/orders.db"


def create_table_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(create_table)
    conn.commit()
    conn.close()


def add_order(size, topping, address):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(insert_order, (size, topping, address))
    conn.commit()
    conn.close()


def get_orders():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(select_orders)
    orders = cursor.fetchall()
    conn.close()
    return orders