sudo gedit /etc/mysql/mysql.cnf

add the below line
-----------------------------------------
[mysqld] 
sql_mode = ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION




sudo apt-get install php-curl
