import aiosqlite
from config import path_db
from database import queries

from database.queries import create_orders_table,create_order_details_table,insert_order,insert_order_details,select_orders



async def init_db():
    async with aiosqlite.connect(path_db) as db:
        await db.execute(create_orders_table)
        await db.execute(create_order_details_table)

        await db.commit()

    print("БД подключена!")


async def add_order(size, address, photo_id):
    async with aiosqlite.connect(path_db) as db:
        cursor = await db.execute(
            insert_order,
            (size, address, photo_id)
        )

        order_id = cursor.lastrowid

        await db.commit()

        return order_id


async def add_order_details(order_id, topping):
    async with aiosqlite.connect(path_db) as db:
        await db.execute(
            insert_order_details,
            (order_id, topping)
        )

        await db.commit()


async def get_orders():
    async with aiosqlite.connect(path_db) as db:
        cursor = await db.execute(select_orders)

        rows = await cursor.fetchall()

        return rows


async def delete_order_by_id(order_id):
    async with aiosqlite.connect(path_db) as db:
        await db.execute(queries.delete_order_details, (order_id,))
        await db.execute(queries.delete_order, (order_id,))

        await db.commit()