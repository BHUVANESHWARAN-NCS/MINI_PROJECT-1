import streamlit as st
import pandas as pd
import mysql.connector
st.title("Retail_Order_Analysis")
st.subheader("10 Qusetions about Retail_Order_Analysis using common table.")
st.write("Select the questions want you want in given below on box.")
query = st.selectbox(
    "SELECT_QUERY:",
    [
        "Top 10 highest revenue generating products",
        "Top 5 cities with the highest profit margins",
        "Total discount given for each category",
        "Average sale price per product category",
        "Region with the highest average sale price",
        "Total profit per category",
        "Top 3 segments with the highest quantity of orders",
        "Average discount percentage given per region",
        "Product category with the highest total profit",
        "Total revenue generated per year"
    ]
)
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nbhuvanesh385",
        database="retail_order"
    )
def run_query(query):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return pd.DataFrame(result)
if query == "Top 10 highest revenue generating products":
    sql = """
    SELECT product_id, SUM(sales_price) AS total_revenue
    FROM retail_orders
    GROUP BY product_id
    ORDER BY total_revenue DESC
    LIMIT 10;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Top 5 cities with the highest profit margins":
    sql = """
    SELECT city, (SUM(profit) / SUM(sales_price)) * 100 AS profit_margin
    FROM retail_orders
    GROUP BY city
    ORDER BY profit_margin DESC
    LIMIT 5;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Total discount given for each category":
    sql = """
    SELECT Category, SUM(discount_price) AS total_discount
    FROM retail_orders
    GROUP BY Category;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Average sale price per product category":
    sql = """
    SELECT Category, AVG(sales_price) AS avg_sale_price
    FROM retail_orders
    GROUP BY Category;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Region with the highest average sale price":
    sql = """SELECT Region, AVG(sales_price) AS avg_sale_price
    FROM retail_orders
    GROUP BY Region
    ORDER BY avg_sale_price DESC
    LIMIT 1;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Total profit per category":
    sql = """
    SELECT Category, SUM(profit) AS total_profit
    FROM retail_orders
    GROUP BY Category;
    """
    df = run_query(sql)
    st.write(df)


elif query == "Top 3 segments with the highest quantity of orders":
    sql ="""SELECT segment, SUM(quantity) AS total_quantity
    FROM retail_orders
    GROUP BY segment
    ORDER BY total_quantity DESC
    LIMIT 3;
    """
    df = run_query(sql)
    st.write(df)

elif query =="Average discount percentage given per region":
    sql = """SELECT Region, AVG(discount_percent) AS avg_discount_percent
    FROM retail_orders
    GROUP BY Region;
    """
    df = run_query(sql)
    st.write(df)

elif query =="Product category with the highest total profit":
    sql ="""SELECT Category, SUM(profit) AS total_profit
    FROM retail_orders
    GROUP BY Category
    ORDER BY total_profit DESC
    LIMIT 1;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Total revenue generated per year":
    sql = """SELECT YEAR(order_date) AS year, SUM(sales_price) AS total_revenue
    FROM retail_orders
    GROUP BY YEAR(order_date)
    ORDER BY year;
    """
    df = run_query(sql)
    st.write(df)

    sql = """DESCRIBE retail_orders;"""

st.subheader("10 Qusetions about Retail_Order_Analysis using join table query.")
st.write("Select the questions want you want in given below on box")
query = st.selectbox(
    "SELECT_QUERY:",
    ["Find all the orders along with product details.",
     "Find the order details where the product's sales price is greater than $100.",
     "List the products and their corresponding orders for a specific country, e.g., UNITED STATES.",
     "Find the total profit for each order.",
     "Get all orders that shipped using 'Standard Class' as the ship mode.",
     "Find the products with the highest discount percentage in each order.",
     "Retrieve all products sold in a specific city.",
     "Find the total quantity of products sold in each order.",
     "List all the products with their categories where the cost price is less than $50.",
     "Find the orders that have FURNITURE product categories."
     ]
)
if query == "Find all the orders along with product details.":
    sql = """
    SELECT orders.order_id, orders.order_date, orders.ship_mode, products.product_id, products.category
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Find the order details where the product's sales price is greater than $100.":
    sql = """
    SELECT orders.order_id, orders.order_date, products.product_id, products.sales_price
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    WHERE products.sales_price > 100;
    """
    df = run_query(sql)
    st.write(df)

elif query == "List the products and their corresponding orders for a specific country, e.g., UNITED STATES.":
    sql = """
    SELECT orders.order_id, orders.country, products.product_id, products.category
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    WHERE orders.country = 'United States';
    """
    df = run_query(sql)
    st.write(df)

elif query == "Find the total profit for each order.":
    sql = """
    SELECT orders.order_id, SUM(products.profit) AS total_profit
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    GROUP BY orders.order_id;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Get all orders that shipped using 'Standard Class' as the ship mode.":
    sql = """
    SELECT orders.order_id, orders.order_date, products.product_id
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    WHERE orders.ship_mode = 'Standard Class';
    """
    df = run_query(sql)
    st.write(df)

elif query == "Find the products with the highest discount percentage in each order.":
    sql = """
    SELECT orders.order_id, products.product_id, products.discount_percent
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    WHERE products.discount_percent = (
        SELECT MAX(discount_percent) 
        FROM products 
        WHERE order_id = orders.order_id
    );
    """
    df = run_query(sql)
    st.write(df)

elif query == "Retrieve all products sold in a specific city.":
    sql = """
    SELECT orders.order_id, orders.city, products.product_id, products.category
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    WHERE orders.city = 'Los Angeles';
    """
    df = run_query(sql)
    st.write(df)

elif query == "Find the total quantity of products sold in each order.":
    sql = """
    SELECT orders.order_id, SUM(products.quantity) AS total_quantity
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    GROUP BY orders.order_id;
    """
    df = run_query(sql)
    st.write(df)

elif query == "List all the products with their categories where the cost price is less than $50.":
    sql = """
    SELECT orders.order_id, products.product_id, products.category
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    WHERE products.cost_price < 50;
    """
    df = run_query(sql)
    st.write(df)

elif query == "Find the orders that have FURNITURE product categories.":
    sql = """
    SELECT orders.order_id, products.category, SUM(products.quantity) AS total_quantity
    FROM orders
    INNER JOIN products ON orders.order_id = products.order_id
    WHERE products.category = 'Furniture'
    GROUP BY orders.order_id;
    """
    df = run_query(sql)
    st.write(df)