# Write your MySQL query statement below
with cte as (
select *, dense_rank() over(partition by departmentId Order by Salary desc) as rank_name from Employee 
)
select d.name as "Department", rt.name as "Employee", salary as "Salary" from (select * from cte where rank_name <= 3) as rt join Department as d on rt.departmentId = d.id; 