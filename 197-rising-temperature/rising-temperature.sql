# Write your MySQL query statement below
-- select id from (
-- select id, temperature , lag(temperature ) over(order by recordDate asc) as temp from weather 
-- ) as b where b.temp is not null and b.temp < b.temperature 

select a.id from Weather  a join Weather  b on datediff(a.recordDate, b.recordDate) = 1
where a.temperature > b.temperature