SELECT * FROM retail_order.retail_orders;
# 1 top 10 highest revenue generating products
SELECT product_id, SUM(sales_price) AS total_revenue
FROM retail_orders
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;
# 2 top 5 cities with the highest profit margins
SELECT city, (SUM(profit) / SUM(sales_price)) * 100 AS profit_margin
FROM retail_orders
GROUP BY city
ORDER BY profit_margin DESC
LIMIT 5;
# 3 total discount given for each category
SELECT Category, SUM(discount_price) AS total_discount
FROM retail_orders
GROUP BY Category;
# 4 average sale price per product category
SELECT Category, AVG(sales_price) AS avg_sale_price
FROM retail_orders
GROUP BY Category;
# 5 region with the highest average sale price
SELECT Region, AVG(sales_price) AS avg_sale_price
FROM retail_orders
GROUP BY Region
ORDER BY avg_sale_price DESC
LIMIT 1;
# 6 total profit per category
SELECT Category, SUM(profit) AS total_profit
FROM retail_orders
GROUP BY Category;
# 7 top 3 segments with the highest quantity of orders
SELECT segment, SUM(quantity) AS total_quantity
FROM retail_orders
GROUP BY segment
ORDER BY total_quantity DESC
LIMIT 3;
# 8 average discount percentage given per region
SELECT Region, AVG(discount_percent) AS avg_discount_percent
FROM retail_orders
GROUP BY Region;
# 9 product category with the highest total profit
SELECT Category, SUM(profit) AS total_profit
FROM retail_orders
GROUP BY Category
ORDER BY total_profit DESC
LIMIT 1;
# 10 total revenue generated per year
SELECT YEAR(order_date) AS year, SUM(sales_price) AS total_revenue
FROM retail_orders
GROUP BY YEAR(order_date)
ORDER BY year;
create table orders(
order_id  INT primary key , 
order_date DATE ,
ship_mode varchar(50),
segment varchar(50),
country varchar(50),
city varchar(50),
state varchar(50),
postal_code int,
region varchar(50)
 );
create table products(
order_id int primary key,
product_id  varchar(50), 
category varchar(50),
sub_category varchar(50),
cost_price float,
list_price float,
sales_price float,
discount_price float,
discount_percent float,
profit float,
quantity int,
foreign key (order_id) references orders(order_id)
);
SELECT orders.order_id,orders.order_date,orders.ship_mode,orders.segment,orders.country,orders.city,orders.state,orders.postal_code,orders.region,
products.order_id,products.product_id,products.category,products.sub_category,products.cost_price,products.list_price,products.sales_price,products.discount_price, products.discount_percent,products.profit,products.quantity
FROM orders orders
INNER JOIN products products ON orders.order_id = products.order_id;
# 11 Find all the orders along with product details.
SELECT orders.order_id, orders.order_date, orders.ship_mode, products.product_id, products.category
FROM orders
INNER JOIN products ON orders.order_id = products.order_id;
# 12 Find the order details where the product's sales price is greater than $100.
SELECT orders.order_id, orders.order_date, products.product_id, products.sales_price
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
WHERE products.sales_price > 100;
# 13. List the products and their corresponding orders for a specific country, e.g., "USA".
SELECT orders.order_id,orders.country, products.product_id, products.category
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
WHERE orders.country = 'United states';
# 14. Find the total profit for each order.
SELECT orders.order_id, SUM(products.profit) AS total_profit
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
GROUP BY orders.order_id;
# 15. Get all orders that shipped using 'Standard Class' as the ship mode.
SELECT orders.order_id, orders.order_date, products.product_id
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
WHERE orders.ship_mode = 'Standard Class';
# 16. Find the products with the highest discount percentage in each order.
SELECT orders.order_id, products.product_id, products.discount_percent
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
WHERE products.discount_percent = (SELECT MAX(discount_percent) FROM products WHERE order_id = orders.order_id);
# 17. Retrieve all products sold in a specific city.
SELECT orders.order_id,orders.city, products.product_id, products.category
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
WHERE orders.city = 'Los Angeles';
# 18. Find the total quantity of products sold in each order.
SELECT orders.order_id, SUM(products.quantity) AS total_quantity
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
GROUP BY orders.order_id;
# 19. List all the products with their categories where the cost price is less than $50.
SELECT orders.order_id, products.product_id, products.category
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
WHERE products.cost_price < 50;
# 20.Find the orders that have "Furniture" product categories.
SELECT orders.order_id, products.category,sum(products.quantity) as total_quantity
FROM orders
INNER JOIN products ON orders.order_id = products.order_id
WHERE products.category IN ('Furniture')
GROUP BY orders.order_id