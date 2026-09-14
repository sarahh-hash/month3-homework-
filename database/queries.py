create_table = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    size TEXT NOT NULL,
    topping TEXT NOT NULL,
    address TEXT NOT NULL
)
"""

insert_order = """
INSERT INTO orders (size, topping, address)
VALUES (?, ?, ?)
"""

select_orders = """
SELECT id, size, topping, address
FROM orders
"""