import streamlit as st
from analyze_data import get_dataframe

st.title("📊 Customer Insights Dashboard")

# Product Sales
df_products = get_dataframe("""
    SELECT p.name AS product, SUM(oi.quantity) AS total_sold
    FROM order_items oi
    JOIN products p ON oi.product_id = p.id
    GROUP BY product
    ORDER BY total_sold DESC;
""")
st.subheader("🛍️ Top Selling Products")
st.bar_chart(df_products.set_index("product"))

# Customer Spending
df_customers = get_dataframe("""
    SELECT c.name AS customer, SUM(oi.quantity * p.price) AS total_spent
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY customer
    ORDER BY total_spent DESC;
""")
st.subheader("💰 Customer Spending")
st.dataframe(df_customers)

# Monthly Revenue
df_months = get_dataframe("""
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
           SUM(oi.quantity * p.price) AS revenue
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY month
    ORDER BY month;
""")
st.subheader("📆 Monthly Revenue")
st.line_chart(df_months.set_index("month"))
