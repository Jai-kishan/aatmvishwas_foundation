show datbases;
SHOW GRANTS FOR asf;

GRANT ALL PRIVILEGES ON *.* TO 'asf'@'localhost' WITH GRANT OPTION;


CREATE USER 'asf' IDENTIFIED BY 'asf@2023';
SELECT user,host FROM mysql.user;
SELECT mysql.user WHERE user='asf';
UPDATE mysql.user SET Host='localhost' WHERE Host='%' AND User='asf';
