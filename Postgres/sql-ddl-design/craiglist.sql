CREATE DATABASE craiglist;

\c craiglist


CREATE TABLE region (
    regionid SERIAL PRIMARY KEY NOT NULL,
    regionname VARCHAR(20)   NOT NULL
);

INSERT INTO region
  (regionid, regionname)
VALUES
   (1, 'San Francisco'),
   (2, 'Atlanta'),
   (3, 'Seattle');


CREATE TABLE users (
    userid SERIAL PRIMARY KEY NOT NULL,
    fname VARCHAR(15)   NOT NULL,
    lname VARCHAR(15)   NOT NULL,
    regionid INTEGER REFERENCES region NOT NULL,
    email TEXT   NOT NULL,
    adress1 VARCHAR(20)   NOT NULL,
    address2 VARCHAR(20)   NOT NULL,
    city VARCHAR(20)   NOT NULL,
    state TEXT   NOT NULL,
    zipcode TEXT   NOT NULL,
    phone TEXT   NOT NULL,
    username VARCHAR(20)   NOT NULL,
    password VARCHAR(20)   NOT NULL
);

INSERT INTO users
  (userid, fname, lname, regionid, email, adress1, address2, city, state, zipcode, phone, username, password)
VALUES
   (1, 'Mary', 'Antony', 1, 'mary@gmail.com', '1 hary rd', '-', 'cary', 'NC', '27511', '789654321', 'maryantony', 'mary345'),
   (2, 'John', 'Chris', 2, 'john@gmail.com', '12 john rd', '-', 'Atlanta', 'GA', '30306', '8976543210', 'johnchris', 'john124'),
   (3, 'Lisa', 'Tony', 3, 'lisa@gmail.com', '323 tony st', '-', 'Columbus', 'OH', '43065', '8067863452', 'lisatony', 'lisa123');

CREATE TABLE category (
    categoryid SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(20)   NOT NULL
);

INSERT INTO category
  (categoryid, name)
VALUES
   (1, 'Auto'),
   (2, 'Real Estate'),
   (3, 'Electronics');

CREATE TABLE post (
    postid SERIAL PRIMARY KEY NOT NULL,
    title TEXT   NOT NULL,
    text TEXT   NOT NULL,
    userid INTEGER REFERENCES users NOT NULL,
    regionid INTEGER REFERENCES region NOT NULL,
    categoryid INTEGER REFERENCES Category NOT NULL,
    adress1 VARCHAR(15)   NOT NULL,
    address2 VARCHAR(15)   NOT NULL,
    city TEXT   NOT NULL,
    state TEXT   NOT NULL,
    zipcode VARCHAR(10)   NOT NULL
);

INSERT INTO post
  (postid, title, text, userid, regionid, categoryid, adress1, address2, city, state, zipcode)
VALUES
   (1, 'Brand New Car', 'Sale', 1, 1, 1, '1 hary rd', '-', 'cary', 'NC', '27511'),
   (2, 'Lovely 2 Bedroom Apartment', 'sale', 2, 2, 1, '12 john rd', '-', 'Atlanta', 'GA', '30306'),
   (3, 'Laptop', 'sale', 3, 3, 1, '323 tony st', '-', 'Columbus', 'OH', '43065');

