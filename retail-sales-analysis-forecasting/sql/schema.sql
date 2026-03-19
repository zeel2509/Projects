CREATE TABLE sales (
    order_id VARCHAR(20),
    order_date DATE,
    product_category VARCHAR(30),
    sub_category VARCHAR(30),
    product_name VARCHAR(80),
    region VARCHAR(20),
    customer_segment VARCHAR(20),
    sales DECIMAL(12,2),
    profit DECIMAL(12,2),
    quantity INT,
    discount DECIMAL(4,2)
);
