create database expense_tracker;

use expense_tracker;

create table user(
    -> uid INT PRIMARY KEY AUTO_INCREMENT,
    -> u_name VARCHAR(100) NOT NULL,
    -> u_num BIGINT NOT NULL UNIQUE);

ALTER TABLE user ADD COLUMN balance DOUBLE;

ALTER TABLE user MODIFY COLUMN balance DECIMAL(10,2) NOT NULL;

ALTER TABLE user ADD COLUMN password VARCHAR(50);

ALTER TABLE user MODIFY COLUMN password VARCHAR(50) NOT NULL;

CREATE TABLE TRANSACTION(
    -> t_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    -> u_id INT NOT NULL,
    -> FOREIGN KEY(u_id) REFERENCES user(uid),
    -> amount DOUBLE(10,2) NOT NULL,
    -> description VARCHAR(50) NOT NULL,
    -> t_date DATE NOT NULL);