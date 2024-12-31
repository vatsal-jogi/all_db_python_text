import sqlite3
cnt=sqlite3.connect('sqlite.db')
# # print(cnt)


# create table
cnt.execute("create table users (id integer primary key, name text(20),email text(50) , password text(50))")
print('table is created')