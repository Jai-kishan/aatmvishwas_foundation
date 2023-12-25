# aatmvishwas_foundation

## Run your cmd as an administrator. It will work.
```
netstat -a -n -o | find "3306"
taskkill /pid 4256 /f   
```


Error
```
WARNINGS:
?: (mysql.W002) MariaDB Strict Mode is not set for database connection 'default'
        HINT: MariaDB's Strict Mode fixes many data integrity problems in MariaDB, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: Num1, admin, auth, contenttypes, sessions

```

solution
```
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Database engine
        'NAME': 'my_project',  #  Name database
        'HOST': 'localhost',  #        ,         
        'PORT': 3306,  # Port 
        'USER': 'root',  #  database username
        'PASSWORD': '',  # Database password
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            'charset': 'utf8mb4'
        }
    }

```


# Your password does not satisfy the current policy requirements
# ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
Because of your password. You can see password validate configuration metrics using the following query in MySQL client:
```
SHOW VARIABLES LIKE 'validate_password%';
```
The output should be something like that :

+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| validate_password.check_user_name    | ON    |
| validate_password.dictionary_file    |       |
| validate_password.length             | 6     |
| validate_password.mixed_case_count   | 1     |
| validate_password.number_count       | 1     |
| validate_password.policy             | LOW   |
| validate_password.special_char_count | 1     |
+--------------------------------------+-------+
then you can set the password policy level lower, for example:

```
SET GLOBAL validate_password.length = 6;
SET GLOBAL validate_password.number_count = 0;
```