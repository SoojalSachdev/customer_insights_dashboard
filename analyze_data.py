import pandas as pd
from db_config import get_connection

def get_dataframe(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Top 5 Selling Products
df1 = get_dataframe("""
    SELECT p.name AS product, SUM(oi.quantity) AS total_sold
    FROM order_items oi
    JOIN products p ON oi.product_id = p.id
    GROUP BY product
    ORDER BY total_sold DESC
    LIMIT 5;
""")
print("Top 5 Selling Products:\n", df1)

# Top Customers by Spend
df2 = get_dataframe("""
    SELECT c.name AS customer, SUM(oi.quantity * p.price) AS total_spent
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY customer
    ORDER BY total_spent DESC;
""")
print("\nTop Customers by Spend:\n", df2)

# Monthly Revenue
df3 = get_dataframe("""
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, 
           SUM(oi.quantity * p.price) AS revenue
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY month
    ORDER BY month;
""")
print("\nMonthly Revenue:\n", df3)
