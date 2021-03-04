# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="student"
)

print(mydb)


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS caserne;")


mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  database="caserne"
)

mycursor = mydb.cursor()
mycursor.execute("""CREATE TABLE IF NOT EXISTS Obstacle (nom VARCHAR(55) NOT NULL PRIMARY KEY, point_bonus TINYINT, 
note_minimale TINYINT) ENGINE=InnoDB;""")
mycursor.execute("""CREATE TABLE IF NOT EXISTS Soldat (matricule VARCHAR(30) NOT NULL PRIMARY KEY, nom VARCHAR(55),
 prenom VARCHAR (55), email VARCHAR(55), grade VARCHAR(55)) ENGINE=InnoDB;""")
mycursor.execute("""CREATE TABLE IF NOT EXISTS Passage (id_passage INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
 nom_obstacle VARCHAR(55) NOT NULL, matricule_soldat VARCHAR(55) NOT NULL, 
 matricule_instructeur VARCHAR(55) NOT NULL, date_passage DATE, note_instructeur TINYINT, 
 temps_passage INT, note_finale TINYINT, 
CONSTRAINT fk_passagesoldat_matricule FOREIGN KEY (matricule_soldat) REFERENCES Soldat(matricule),
CONSTRAINT fk_passageinstructeur_matricule FOREIGN KEY (matricule_instructeur) REFERENCES Soldat(matricule),
CONSTRAINT fk_passageobstacle_nom FOREIGN KEY (nom_obstacle) REFERENCES Obstacle(nom))
ENGINE=InnoDB;""")

mycursor.execute("""INSERT INTO Obstacle (note_minimale, point_bonus, nom) VALUES (10,0,'Barres'),
(12,1,'Tranchée'), (11,1,'Barbelé'), (15,0,'Vitesse'), (13,0,'Endurance'), (14,1,'Tir');
""")

mycursor.execute("""INSERT INTO Soldat (matricule, nom, prenom, email, grade) VALUES
('0000','Dupont','Bernard','Beber@armee.fr','Sergent'),
('0001','Martin','Albert','Beberlevrai@armee.fr','Première classe'),
('0002','Schmidt','Olivia','Olivia@armee.fr','Lieutenant'),
('0003','Muller','Jean','Jeannot@armee.fr','Seconde classe'),
('0004','Dubois','Irene','LaBoss@armee.fr','Générale');
""")

mycursor.execute("""INSERT INTO Passage (nom_obstacle, matricule_soldat, matricule_instructeur,
date_passage, note_instructeur, temps_passage, note_finale) VALUES
('Barbelé', '0000','0004',20210303, 14, 345, 15),
('Vitesse', '0000','0004',20210303, 9, 102, 9),
('Barbelé', '0003','0001',20210201, 8, 582, 9),
('Tranchée', '0002','0000',20210215, 18, 58, 19),
('Tir', '0004','0002',20210103, 13, 85, 14);
""")

mydb.commit()


mycursor.execute("SELECT * FROM Obstacle")
print("Table Obstacle :")
for x in mycursor:
  print(x)

mycursor.execute("SELECT * FROM Soldat")
print("Table Soldat :")
for x in mycursor:
  print(x)

mycursor.execute("SELECT * FROM Passage")
print("Table Passage :")
for x in mycursor:
  print(x)


mycursor.execute("UPDATE Obstacle SET note_minimale = 14 WHERE nom = 'Vitesse'")
mycursor.execute("UPDATE Soldat SET email='Olivialc@armee.fr', grade='Lieutenant colonel' WHERE matricule='0002'")
mycursor.execute("UPDATE Passage SET note_instructeur = '10', temps_passage = 482, note_finale = 11 WHERE id_passage = 2")

mydb.commit()

mycursor.execute("SELECT * FROM Obstacle")
print("Table Obstacle modifiée :")
for x in mycursor:
  print(x)

mycursor.execute("SELECT * FROM Soldat")
print("Table Soldat modifiée :")
for x in mycursor:
  print(x)

mycursor.execute("SELECT * FROM Passage")
print("Table Passage modifiée :")
for x in mycursor:
  print(x)

mycursor.execute("DELETE FROM Passage WHERE date_passage=20210201")
mydb.commit()

mycursor.execute("SELECT * FROM Passage")
print("Table Passage avec tuple supprimé :")
for x in mycursor:
  print(x)

