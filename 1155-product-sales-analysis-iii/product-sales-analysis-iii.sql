# Write your MySQL query statement below
with early_year as 
(
    select product_id, min(year) as first_year from Sales group by product_id
)
select s.product_id, ey.first_year, s.quantity, s.price from Sales as s join early_year as ey on s.year = ey.first_year and s.product_id = ey.product_id