import sqlite3
# users -> id,username,password
# Diseases -> id,dieseasename,symptoms 
if __name__ == "__main__":
	con = sqlite3.connect("healthcare.db")

	con.execute("create table users(id int primary key, username varchar(60), password varchar(60))")
	con.execute("create table dieseases(id int primary key, dieseasename varchar(60), symptoms varchar(500))")