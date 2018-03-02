#Create database table and populate it with data

import sqlite3

with sqlite3.connect("blog.db") as conn:
	c = conn.cursor()
	
	#create the table
	c.execute("""CREATE TABLE Posts
	         (Title TEXT, Post TEXT)""")
	         
	#insert dummy data
	data = (("Good","I'm Good"),
	        ("Well","I'm Well"),
	        ("Excellent","I'm Execellent"),
	        ("Okay","I'm Okay"))
	        
	c.executemany("""INSERT INTO Posts VALUES(?,?)""",data)
