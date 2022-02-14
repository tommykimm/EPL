import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="12345",
  database="practice"
)


#1-Comments
#a) deleting elements in table -> change name by teams
mycursor = mydb.cursor()
sql = "DELETE FROM practice.astonvilla"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

#b) table creation -> To change name of table by teams
# mycursor = mydb.cursor()
# sql = "CREATE TABLE wolves ( id INT(30) NOT NULL,  comment VARCHAR(30) NOT NULL);"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "table(s) created")



# #2 Change points -> To change by team id no.
# # a) table creation -> To change points in seasons by teams
# mycursor = mydb.cursor()
# sql = "UPDATE `practice`.`points` SET `points_8` = '61' WHERE (`id` = '1');"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "point(s) changed")


# #3Change goals -> To change by player id
# mycursor = mydb.cursor()
# sql = "UPDATE `practice`.`topscorers` SET `Goals` = '13' WHERE (`id` = '154');"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "goal(s) changed")


# #4Change results -> To change score manually
# mycursor = mydb.cursor()
# sql = "UPDATE `practice`.`scores` SET `scores` = '3-0' WHERE (`id` = '419');"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "score(s) changed")
