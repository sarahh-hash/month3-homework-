create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    size TEXT NOT NULL,
    address TEXT NOT NULL,
    photo_id TEXT NOT NULL
)
"""

create_order_details_table = """
CREATE TABLE IF NOT EXISTS order_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    topping TEXT NOT NULL
);
"""


insert_order = """
INSERT INTO orders (size, address, photo_id)
VALUES (?, ?, ?)
"""

insert_order_details = """
INSERT INTO order_details (order_id, topping)
VALUES (?, ?);
"""

select_orders = """
SELECT
    orders.id,
    orders.size,
    orders.address,
    orders.photo_id,
    order_details.topping
FROM orders
INNER JOIN order_details
ON orders.id = order_details.order_id
"""

delete_order = """
DELETE FROM orders WHERE id = ?
"""

delete_order_details = """
DELETE FROM order_details WHERE order_id = ?
"""