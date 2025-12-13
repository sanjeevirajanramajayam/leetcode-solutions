# Write your MySQL query statement below
select tot.user_id, COALESCE(ROUND(confirm_count / total, 2), 0) as confirmation_rate from (select user_id, count(user_id) as confirm_count from Confirmations where action = 'confirmed' group by user_id) as tou RIGHT JOIN (select su.user_id, count(c.user_id) as total from Confirmations c RIGHT JOIN Signups su on c.user_id = su.user_id group by su.user_id) as tot on tou.user_id = tot.user_id 

-- (select su.user_id, count(c.user_id) as total from Confirmations c RIGHT JOIN Signups su on c.user_id = su.user_id group by su.user_id)

-- (select su.user_id, count(c.user_id) as confirm_count from Confirmations c RIGHT JOIN Signups su on c.user_id = su.user_id group by su.user_id)