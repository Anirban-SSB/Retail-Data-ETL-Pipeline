-- total revenue
SELECT SUM(revenue) AS total_revenue
FROM sales;

--revenue by product category
SELECT category, SUM(revenue) AS revenue_by_category
FROM sales
GROUP BY category;

-- revenue by country
SELECT country, SUM(revenue) AS revenue_by_country
FROM sales
GROUP BY country
ORDER BY revenue_by_country DESC; 
