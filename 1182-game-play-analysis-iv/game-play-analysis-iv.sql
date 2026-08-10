# Write your MySQL query statement below
with p as (select count(*) as count from (select player_id, min(event_date) as event_date from activity group by player_id) as a join activity b on a.player_id = b.player_id and a.event_date = DATE_SUB(b.event_date, INTERVAL 1 DAY))
select round(p.count / COUNT(DISTINCT player_id), 2) as fraction from Activity join p
-- select * from p