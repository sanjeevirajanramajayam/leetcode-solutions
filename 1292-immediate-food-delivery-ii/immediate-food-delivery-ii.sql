# Write your MySQL query statement below
WITH first_orders as (
    SELECT customer_id, MIN(order_date) as od_date from Delivery group by customer_id
)
select round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) * 100 / count(delivery_id), 2) as immediate_percentage from Delivery d join first_orders f on d.customer_id = f.customer_id and d.order_date = f.od_date;