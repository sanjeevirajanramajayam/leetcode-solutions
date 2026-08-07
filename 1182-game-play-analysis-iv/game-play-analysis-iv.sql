# Write your MySQL query statement below
select round(((select count(*) from activity a1 join (select min(event_date) as event_date, player_id from activity group by player_id) a2 on a1.player_id = a2.player_id and datediff(a1.event_date, a2.event_date) = 1) / (select count(distinct player_id ) from activity)),2) as fraction
