# UDFs-written-in-Python
MySQL UDFs written in Python

# Compiled as:
```
gcc $(/home/sh/REPOS/MYSQL_DEV_ACTIONS/mysql-5.7/mysql-server/5.7.16/bin/mysql_config --cflags) -fPIC -shared -o factorial.so factorial.cc
```
# Activated as:
```
cp factorial.so /home/sh/REPOS/MYSQL_DEV_ACTIONS/mysql-5.7/mysql-server/5.7.16/lib/plugin/
cp factorial.py /home/sh/REPOS/MYSQL_DEV_ACTIONS/mysql-5.7/mysql-server/5.7.16/lib/plugin/

create function factorial returns integer soname 'factorial.so';
```
