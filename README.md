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


Unable to activate the evironment 
```File C:\Users\ltim\venv\asf_env\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more
information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:3
+ . .\asf_env\Scripts\Activate.ps1
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess```

Solution:

As an Administrator, you can set the execution policy by typing this into your PowerShell window:

```
Set-ExecutionPolicy RemoteSigned
```

For more information, see Using the Set-ExecutionPolicy Cmdlet.

When you are done, you can set the policy back to its default value with:

```
Set-ExecutionPolicy Restricted
```

You may see an error:

Access to the registry key
```
'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell' is denied. 
To change the execution policy for the default (LocalMachine) scope, 
  start Windows PowerShell with the "Run as administrator" option. 
To change the execution policy for the current user, 
  run "Set-ExecutionPolicy -Scope CurrentUser".
```
So you may need to run the command like this (as seen in comments):

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
