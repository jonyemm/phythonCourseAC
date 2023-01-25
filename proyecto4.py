rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
tiro_de_usuario = int (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
tiro_de_computadora = random.randint(0,2)

def game(tiro, jugador):
    print(jugador)
    if tiro == 0:
        print(rock)
    elif tiro == 1:
        print(paper)
    elif tiro == 2:
        print(scissors)

def ganador(usuario,computadora):
    if usuario == 0 and computadora == 2:
        print("Gana USUARIO")
    elif computadora == 0 and usuario == 2:
        print("Gana COMPUTADORA")
    elif usuario == 2 and computadora == 1:
        print("Gana USUARIO")
    elif computadora == 2 and usuario == 1:
        print("Gana COMPUTADORA")
    elif usuario == 1 and computadora == 0:
        print("Gana USUARIO")
    elif computadora == 1 and usuario == 0:
        print("Gana COMPUTADORA")
    else:
        print("EMPATE")

game(tiro_de_usuario,"USUARIO")
game(tiro_de_computadora,"COMPUTADORA")
ganador(tiro_de_usuario,tiro_de_computadora)




