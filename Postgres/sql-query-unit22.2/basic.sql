--More SQL (Including aggregates)
--1. For this challenge you need to create a simple SELECT statement that will return all columns from the people table WHERE their age is over 50

-- people table schema
-- id
-- name
-- age
-- You should return all people fields where their age is over 50 and order by the age descending

-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
SELECT * FROM people WHERE age > 50 ORDER BY age DESC;

-- 2. For this challenge you need to create a simple SUM statement that will sum all the ages.

-- people table schema
-- id
-- name
-- age
-- select table schema
-- age_sum (sum of ages)
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

-- NOTE2: You need to use ALIAS for creating age_sum
SELECT SUM(age) as age_sum FROM people;

-- 3. For this challenge you need to create a simple MIN / MAX statement that will return the Minimum and Maximum ages out of all the people.

-- people table schema
-- id
-- name
-- age
-- select table schema
-- age_min (minimum of ages)
-- age_max (maximum of ages)
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
SELECT MIN(age) AS age_min, MAX(age) AS age_max FROM people;

-- 4.Create a simple SELECT query to display student information of all ACTIVE students.

-- TABLE STRUCTURE:

-- students
-- Id	FirstName	LastName	IsActive

-- Note: IsActive (true or false)
SELECT * FROM students WHERE IsActive;

-- 5. For this challenge you need to create a simple GROUP BY statement, you want to group all the people by their age and count the people who have the same age.

-- people table schema
-- id
-- name
-- age
-- select table schema
-- age [group by]
-- people_count (people count)
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.
SELECT age, count(age) as people_count FROM people GROUP BY age HAVING COUNT(age) > 1;

-- 6. For this challenge you need to create a simple HAVING statement, you want to count how many people have the same age and return the groups with 10 or more people who have that age.

-- people table schema
-- id
-- name
-- age
-- return table schema
-- age
-- total_people
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.


SELECT age, count(age) as total_people FROM people GROUP BY age HAVING count(age) >= 10;

