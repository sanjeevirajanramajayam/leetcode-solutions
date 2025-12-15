# Write your MySQL query statement below
select name as results from (
select count(*) as count, name, u.user_id from MovieRating as mr join Users as u on mr.user_id = u.user_id
group by u.user_id 
order by count desc, name
limit 1) as p
UNION ALL
select title as results from (
select title, avg(rating) as avg from MovieRating mr join Movies m on m.movie_id = mr.movie_id where YEAR(created_at) = 2020 and MONTH(created_at) = 2 group by mr.movie_id order by avg desc, title limit 1) as d