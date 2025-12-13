# Write your MySQL query statement below
select MAX(num) as num from (select * from MyNumbers group by num having count(num) = 1) as single