# Write your MySQL query statement below
select temp2.product_id, COALESCE(p.new_price, 10) as price from (select product_id, max(change_date) as new_change_date, change_date from products  where change_date <= '2019-08-16' group by product_id) as temp join products p right join (select distinct product_id from products) as temp2
 on p.product_id = temp.product_id and p.change_date = temp.new_change_date and temp2.product_id = p.product_id
-- select distinct product_id from products