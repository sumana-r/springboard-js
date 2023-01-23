-- write your queries here
-- Join the two tables so that every column and record appears.
Select v.id,o.first_name,o.last_name,v.make,v.model,v.year,v.price,v.owner_id from owners o full outer join vehicles v on o.id = v.owner_id;
Select * from owners o full outer join vehicles v on o.id = v.owner_id;

--Count the number of cars for each owner. Display the owners first_name, last_name and count of vehicles.
Select first_name,last_name,count(owner_id) from owners o Join vehicles v on o.id = v.owner_id group by first_name, last_name order by first_name;

-- Count the number of cars for each owner and display the average price for each of the cars as integers. 
-- Display the owners first_name, last_name, average price and count of vehicles. The first_name should be ordered in descending order. 
-- Only display results with more than one vehicle and an average price greater than 10000. Your output should look like this:

Select first_name, last_name, round(avg(price)) as average_price, count(owner_id) from owners o Join vehicles v on o.id=v.owner_id 
group by first_name, last_name having count(owner_id) > 1 and round(avg(price)) > 10000 
order by first_name DESC;