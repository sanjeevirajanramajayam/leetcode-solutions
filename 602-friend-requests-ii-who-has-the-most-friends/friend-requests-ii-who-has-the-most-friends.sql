# Write your MySQL query statement below
select p.temp as id, count(*) as num from (
select requester_id as temp from RequestAccepted
union all
select accepter_id  as temp from RequestAccepted 
) p group by p.temp order by count(*) desc limit 1