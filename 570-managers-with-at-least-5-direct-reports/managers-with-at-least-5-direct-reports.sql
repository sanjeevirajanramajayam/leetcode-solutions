# Write your MySQL query statement below
select name from (select managerId as reports from Employee group by managerId having count(reports) >= 5) as five JOIN Employee as e on five.reports = e.id