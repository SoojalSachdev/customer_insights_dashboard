from db_config import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert sample customers
    customers = [("John Doe", "john@example.com"),
                 ("Alice Smith", "alice@example.com")]
    cursor.executemany("INSERT INTO customers (name, email) VALUES (%s, %s)", customers)

    # Insert sample products
    products = [("Product A", 25.5),
                ("Product B", 35.0),
                ("Product C", 15.0)]
    cursor.executemany("INSERT INTO products (name, price) VALUES (%s, %s)", products)

    # Insert orders
    orders = [(1, "2024-04-01"),
              (2, "2024-04-02"),
              (1, "2024-04-03")]
    cursor.executemany("INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)", orders)

    # Insert order items
    order_items = [(1, 1, 2), (1, 2, 1),
                   (2, 3, 4),
                   (3, 1, 1), (3, 2, 2)]
    cursor.executemany("INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)", order_items)

    conn.commit()
    cursor.close()
    conn.close()
    print("Data seeded successfully!")

if __name__ == "__main__":
    seed_data()
