# Write your MySQL query statement below
WITH test as (select machine_id, SUM(CASE WHEN activity_type = 'start' THEN -1 * timestamp else timestamp END) as process_time from Activity group by machine_id, process_id)

select machine_id, ROUND(avg(process_time),3) as processing_time from test group by machine_id;