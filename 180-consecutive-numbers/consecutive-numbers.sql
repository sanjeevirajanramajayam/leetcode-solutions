# Write your MySQL query statement below
select DISTINCT a.num as ConsecutiveNums from LOGS a join LOGS b join LOGS c on a.num = b.num and b.num = c.num and  b.id = a.id + 1 and c.id = b.id + 1 