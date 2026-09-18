import aiosqlite

from database.queries import (
    create_orders_table,
    create_order_details_table,
    insert_order,
    insert_order_details,
    select_orders
)


path_db = "database/sqlite3.db"


async def init_db():
    async with aiosqlite.connect(path_db) as db:
        await db.execute(create_orders_table)
        await db.execute(create_order_details_table)

        await db.commit()

    print("БД подключена!")


async def add_order(size, address):
    async with aiosqlite.connect(path_db) as db:
        cursor = await db.execute(
            insert_order,
            (size, address)
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

        orders = await cursor.fetchall()

        return orders