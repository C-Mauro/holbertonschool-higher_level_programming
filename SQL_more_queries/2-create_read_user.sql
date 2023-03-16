-- create a database hbtn_0d_2
-- create user user_0d_2

CREATE database IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS `user_0d_2` IDENTIFIED BY `hbtn_0d_2`;
GRANT SELECT ON *.* `user_0d_1`@`localhost`;
