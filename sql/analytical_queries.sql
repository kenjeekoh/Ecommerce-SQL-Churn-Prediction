-- =============================
-- E-Commerce Analytics Queries
-- =============================


-- ============================================================
-- 1. Total Revenue by Product Category
SELECT 
    p.category,
    ROUND(SUM(oi.quantity * oi.price_each), 2) AS total_revenue
FROM 
    Order_Items oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY 
    p.category
ORDER BY 
    total_revenue DESC;
-- ============================================================


-- ============================================================
-- 2. Top Customers by Total Spend
SELECT 
    c.name AS customer_name,
    ROUND(SUM(oi.quantity * oi.price_each), 2) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 10;
-- ============================================================


-- ============================================================
-- 3. Monthly Revenue Trends
SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    ROUND(SUM(oi.quantity * oi.price_each), 2) AS monthly_revenue
FROM Orders o
JOIN Order_Items oi ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;
-- ============================================================


-- ============================================================
-- 4. Average Order Value by Region
SELECT 
    c.region,
    ROUND(SUM(oi.quantity * oi.price_each) / COUNT(DISTINCT o.order_id), 2) AS avg_order_value
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
GROUP BY c.region
ORDER BY avg_order_value DESC;
-- ============================================================


-- ============================================================
-- 5. Repeat Customers (More than One Order)
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING total_orders > 1
ORDER BY total_orders DESC;
-- ============================================================