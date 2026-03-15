-- SQL to create sales table matching the current dataset and transformation
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER,
    customer_id TEXT,
    product TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER,
    date TEXT,
    country TEXT,
    revenue REAL
);