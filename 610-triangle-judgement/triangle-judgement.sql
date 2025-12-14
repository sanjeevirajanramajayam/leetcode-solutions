# Write your MySQL query statement below
select *, CASE WHEN (t.x + t.y > t.z and t.y + t.z > t.x and t.z + t.x > t.y) THEN "Yes" ELSE "No" END AS triangle from triangle t;