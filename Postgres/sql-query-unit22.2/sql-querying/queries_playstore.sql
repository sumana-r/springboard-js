-- Comments in SQL Start with dash-dash --
-- Google Play Store Querying

-- Find the app with an ID of 1880.
SELECT * FROM analytics WHERE id = 1880;

-- Find the ID and app name for all apps that were last updated on August 01, 2018.
SELECT id, app_name FROM analytics WHERE last_updated = '2018-08-01';

-- Count the number of apps in each category, e.g. “Family | 1972”.
SELECT category, COUNT(*) FROM analytics GROUP BY category;

-- Find the top 5 most-reviewed apps and the number of reviews for each.
SELECT * FROM analytics ORDER BY reviews DESC LIMIT 5;

-- Find the app that has the most reviews with a rating greater than equal to 4.8.
SELECT * FROM analytics WHERE rating >= 4.8 ORDER BY reviews DESC LIMIT 1;

-- Find the average rating for each category ordered by the highest rated to lowest rated.
SELECT category, AVG(rating) as avg_rating FROM analytics GROUP BY category ORDER BY avg_rating DESC;

-- Find the name, price, and rating of the most expensive app with a rating that’s less than 3.
SELECT app_name, price, rating FROM analytics WHERE rating < 3 ORDER BY price DESC LIMIT 1;

-- Find all apps with a min install not exceeding 50, that have a rating. Order your results by highest rated first.
SELECT * FROM analytics WHERE min_installs <=50 AND rating IS NOT NULL ORDER BY rating DESC;

-- Find the names of all apps that are rated less than 3 with at least 10000 reviews.
SELECT app_name FROM analytics WHERE rating < 3 and reviews >= 10000;

-- Find the top 10 most-reviewed apps that cost between 10 cents and a dollar.
SELECT * FROM analytics WHERE price BETWEEN 0.1 AND 1 ORDER BY reviews DESC LIMIT 10;

-- Find the most out of date app. Hint: You don’t need to do it this way, but it’s possible to do with a subquery: http://www.postgresqltutorial.com/postgresql-max-function/
SELECT * FROM analytics WHERE last_updated = (SELECT MIN(last_updated) FROM analytics);

-- Find the most expensive app (the query is very similar to #11).
SELECT * FROM analytics WHERE price = (SELECT MAX(price) FROM analytics);

-- Count all the reviews in the Google Play Store.
SELECT SUM(reviews) AS "all_reviews" FROM analytics;

-- Find all the categories that have more than 300 apps in them.
SELECT category FROM analytics GROUP BY category HAVING COUNT(*) > 300;

-- Find the app that has the highest proportion of min_installs to reviews, among apps that have been installed at least 100,000 times. Display the name of the app along with the number of reviews, the min_installs, and the proportion.
SELECT app_name, reviews, min_installs,  min_installs / reviews AS highest_proportion FROM analytics WHERE min_installs >= 100000 ORDER BY highest_proportion DESC LIMIT 1;

