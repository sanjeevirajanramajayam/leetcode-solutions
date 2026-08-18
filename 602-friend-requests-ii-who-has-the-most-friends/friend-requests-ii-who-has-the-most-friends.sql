# Write your MySQL query statement below
select requester_id as id, count(*) as num from (
select requester_id from RequestAccepted 
UNION ALL
select accepter_id  from RequestAccepted 
) b group by requester_id order by count(*) desc limit 1