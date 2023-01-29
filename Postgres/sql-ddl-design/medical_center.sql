DROP DATABASE IF EXISTS medical_center;
CREATE DATABASE medical_center;

\c medical_center

CREATE TABLE medical_center (
    medical_center_id SERIAL PRIMARY KEY  NOT NULL,
    name VARCHAR(15) NOT NULL,
    adress1 VARCHAR(20) NOT NULL,
    address2 VARCHAR(20) NOT NULL,
    city TEXT NOT NULL,
    State TEXT NOT NULL,
    ZipCode VARCHAR(10) NOT NULL,
    Phone TEXT   NOT NULL
    );

INSERT INTO medical_center
  (medical_center_id, name, adress1, address2, city, State, ZipCode, Phone)
VALUES
  (1, 'CMS', '1001 stone','willow' , 'Chicago', 'IL', '60007', '9876543201'),
  (2, 'MMS',  '1021 silver', 'bay', 'New York', 'NY', '10006', '8979675654');
  


CREATE TABLE doctor (
    doctor_id SERIAL PRIMARY KEY  NOT NULL,
    name VARCHAR(15)   NOT NULL ,
    gender VARCHAR(12)   NOT NULL,
    email VARCHAR(50)   NOT NULL,
    adress1 VARCHAR(20)   NOT NULL,
    address2 VARCHAR(20)   NOT NULL,
    city TEXT   NOT NULL,
    state TEXT   NOT NULL,
    zipcode VARCHAR(10)   NOT NULL,
    phone TEXT NOT NULL
);

INSERT INTO doctor
  (doctor_id, name, gender, email, adress1, address2, city, State, ZipCode, Phone)
VALUES
  (1, 'Erin', 'female', 'erin@gmail.com', '100 stone','willow' , 'Chicago', 'IL', '60007', '9876543210'),
  (2, 'John', 'male', 'john@yahoo.com', '102 silver', 'bay', 'New York', 'NY', '10006', '8979675645'),
  (3, 'Johnson', 'male', 'johnson@gmail.com', '103 courtney', 'coarse', 'Cary', 'NC', '27511', '789654321'),
  (4, 'Nick', 'male', 'nick@hotmail.com', '104 courtney', 'sea', 'Atlanta', 'GA', '30306', '7049877654'),
  (5, 'Maria', 'female', 'maria@gmail.com', '105 parkire', 'drive', 'Columbus', 'OH', '43065', '8067863452');
 


CREATE TABLE patient (
    patientid SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(15)   NOT NULL,
    gender VARCHAR(12)   NOT NULL,
    email VARCHAR(50)   NOT NULL,
    adress1 VARCHAR(20)   NOT NULL,
    address2 VARCHAR(20)   NOT NULL,
    city TEXT   NOT NULL,
    state TEXT   NOT NULL,
    zipCode VARCHAR(10)   NOT NULL,
    phone TEXT   NOT NULL
    
);

INSERT INTO patient
  (patientid, name, gender, email, adress1, address2, city, State, ZipCode, Phone)
VALUES
  (1, 'Jessy', 'female', 'jessy@gmail.com', '2100 stone','willow' , 'Chicago', 'IL', '60007', '9875643210'),
  (2, 'Antony', 'male', 'antony@yahoo.com', '3102 silver', 'bay', 'New York', 'NY', '10006', '8979645645');
 

CREATE TABLE medical_center_employees (
    employeeid INTEGER REFERENCES doctor(doctor_id)  NOT NULL,
    medical_center_id INTEGER REFERENCES medical_center(medical_center_id)  NOT NULL
);

CREATE TABLE visits (
    visitid SERIAL PRIMARY KEY NOT NULL,
    patientid INTEGER REFERENCES patient(patientid)  NOT NULL,
    doctorid INTEGER REFERENCES doctor(doctor_id) NOT NULL,
    visitdate Date   NOT NULL,
    summary TEXT  NOT NULL    
);

INSERT INTO visits
  (visitid, patientid, doctorid, visitdate, summary)
VALUES
  (1, 1, 1, '12-02-2022', 'Stomach Ache'),
  (2, 2, 2, '11-01-2023', 'Head Ache');
 

