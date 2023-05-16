-- drop all tables
DROP DATABASE IF EXISTS hospitalDB;
-- 
CREATE DATABASE hospitalDB;
USE hospitalDB;
SELECT DATABASE();
SHOW TABLES;
--                 
DROP TABLE IF EXISTS patient_details;
DROP TABLE IF EXISTS doctor_details;
DROP TABLE IF EXISTS nurse_details;
DROP TABLE IF EXISTS other_workers_details;
DROP TABLE IF EXISTS user_data;
-- 
-- create doctor_details table
CREATE TABLE IF NOT EXISTS doctor_details(
d_id INT AUTO_INCREMENT,
d_name VARCHAR(30) NOT NULL,
d_spec VARCHAR(50) DEFAULT 'General',
d_age INT, -- d_dob DATE,
d_addrs VARCHAR(70),
d_contact VARCHAR(15),
d_fees DECIMAL(6,0) DEFAULT '1000',
d_msalary DECIMAL(6, 0) DEFAULT '45000',
-- p_id INT,
PRIMARY KEY (d_id)
);
USE hospitalDB;
SELECT * FROM doctor_details;
DESC doctor_details;
DROP TABLE IF EXISTS doctor_details;
-- create nurse_details table
CREATE TABLE IF NOT EXISTS nurse_details(
n_id INT AUTO_INCREMENT,
n_name VARCHAR(30),
n_age INT, -- n_dob DATE,
n_address VARCHAR(30),
n_contact VARCHAR(15),
n_msalary INT DEFAULT '25000',
-- p_id INT,
PRIMARY KEY (n_id)
);
USE hospitalDB;
SELECT * FROM nurse_details;
DESC nurse_details;
DROP TABLE IF EXISTS nurse_details;
-- create other_workers_details table
-- might avoid using this, seems 
/*CREATE TABLE IF NOT EXISTS other_workers_details(
o_id INT AUTO_INCREMENT,
o_name VARCHAR(30),
o_age INT, -- o_dob DATE,
o_address VARCHAR(30),
o_contact VARCHAR(15),
o_msalary DECIMAL(6, 0) DEFAULT '15000',
p_id INT,
PRIMARY KEY (o_id),
FOREIGN KEY (p_id) REFERENCES patient_details(p_id)
);
USE hospitalDB;
SELECT * FROM other_workers_details;
DESC other_workers_details;
DROP TABLE IF EXISTS other_workers_details; */
-- create patient_details table
CREATE TABLE IF NOT EXISTS patient_details(
p_id INT AUTO_INCREMENT,
p_name VARCHAR(30),
p_gender VARCHAR(15),
p_age INT, -- p_dob DATE,
p_addrs VARCHAR(50),
p_contact VARCHAR(15),
d_id INT,
n_id INT,
PRIMARY KEY (p_id),
FOREIGN KEY (d_id) REFERENCES doctor_details(d_id),
FOREIGN KEY (n_id) REFERENCES nurse_details(n_id)
-- ,FOREIGN KEY (o_id) REFERENCES nurse_details(o_id)
);
USE hospitalDB;
SELECT * FROM patient_details;
DESC patient_details;
DROP TABLE IF EXISTS patient_details;
-- create user_data table
CREATE TABLE IF NOT EXISTS user_data(
unm VARCHAR(30),
pword VARCHAR(30) DEFAULT'000',
reg_name VARCHAR(40),
urole VARCHAR(15),
PRIMARY KEY (unm)
);
USE hospitalDB;
SELECT * FROM user_data;
DESC user_data;
DROP TABLE IF EXISTS user_data;
-- ------------------------
INSERT INTO user_data (unm, pword, reg_name, urole) VALUES("admin","admin123","Nerd Admin","admin"),("manager","manager123","Nerd Manager","manager"),
("tpa","tpa123", "Nerd TPA", "tpa"), ("receptionist","receptionist123","Nerd Receptionist","receptionist"),("doctor","doctor123","Dr. Nerd", "doctor");