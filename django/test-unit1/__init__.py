import mysql.connector
from person import Person

personne1 = Person("Jean Baptiste", "Prince Stanley", 31)


cnx = mysql.connector.connect(
    host="192.168.17.250",
    user="root",
    password="mysql",
    database="person"
)

cursor = cnx.cursor()

query = "INSERT INTO person (nom, prenom, age) VALUES (%s, %s, %s)"
values = (personne1.nom, personne1.prenom, personne1.age)

cursor.execute(query, values)

cursor.close()
cnx.close()
