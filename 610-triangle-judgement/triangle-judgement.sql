# Write your MySQL query statement below
select *, (case when p.x + p.y > p.z and p.x + p.z > p.y and p.y + p.z > p.x then "Yes" else "No" end) as triangle from triangle p