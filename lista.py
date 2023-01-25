# Fernanda 
# Melisa del Carmen
# José
# Miriam Janet
# Natalia
# Tamara
# Jasive 
# Gabriel
# Jonathan Palacios (Emmanuel)
# Kenia
# Rodrigo
# Luis
# Yamil
# Cinthia Melisa
# Miguel
import random

nombres = ["Alejandro","Fernanda", "Melisa", "Jose", "Miriam", "Natalia", "Tamara", "Jasive", "Gabriel", "Emmanuel", "Kenia", "Rodrigo", "Luis", "Yamil", "Cinthia", "Miguel"]
#print(nombres[random.randint(0,len(nombres)-1)])

with open("liste.txt") as liste:
    lineas = liste.readlines()
    print(lineas[random.randint(0,len(nombres)-1)])

