CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        select c.salary from (select b.*, ROW_NUMBER() OVER (order by salary desc) as id from (select distinct salary from Employee order by salary desc) b) c where c.id = N
  );
END
-- select *, ROW_NUMBER() OVER (order by id) from Employee
