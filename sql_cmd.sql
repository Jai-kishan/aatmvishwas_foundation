show databases;
create database asf_db;
SHOW GRANTS FOR asf;

GRANT ALL PRIVILEGES ON *.* TO 'asf'@'localhost' WITH GRANT OPTION;


CREATE USER 'asf' IDENTIFIED BY 'asf@2023';
SELECT user,host FROM mysql.user;
SELECT mysql.user WHERE user='asf';
UPDATE mysql.user SET Host='localhost' WHERE Host='%' AND User='asf';



sudo mysql -u root # I had to use "sudo" since it was a new installation

mysql> USE mysql;
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
mysql> CREATE DATABASE asf_db;
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> exit;





SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'apps_program';

ALTER TABLE program ADD FOREIGN KEY (program_brief) REFERENCES program(program_brief);
ALTER TABLE program ADD FOREIGN KEY (program_brief) REFERENCES program_heading;(id);


ALTER TABLE program ADD program_brief varchar(255);