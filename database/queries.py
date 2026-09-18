create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    size TEXT NOT NULL,
    address TEXT NOT NULL
);
"""

create_order_details_table = """
CREATE TABLE IF NOT EXISTS order_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    topping TEXT NOT NULL
);
"""

insert_order = """
INSERT INTO orders (size, address)
VALUES (?, ?);
"""

insert_order_details = """
INSERT INTO order_details (order_id, topping)
VALUES (?, ?);
"""

select_orders = """
SELECT orders.order_id,
       orders.size,
       order_details.topping,
       orders.address
FROM orders
INNER JOIN order_details
ON orders.order_id = order_details.order_id;
"""