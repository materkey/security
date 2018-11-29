import sqlite3
conn = sqlite3.connect('users.db')

c = conn.cursor()
#login = raw_input("Enter UserLogin to add new user: ")
password = input("Enter UserPass to add new user:\n")
c.executescript("insert into Users(UserLogin, UserPass) values('newuser' , '%s')" % password )

c.execute("select UserLogin from Users")
for row in c.fetchall():
  print(row)

conn.commit()

conn.close()
