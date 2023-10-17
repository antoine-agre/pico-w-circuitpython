from Serveur import Serveur
import time
import board
from digitalio import DigitalInOut, Pull, Direction
from analogio import AnalogIn

# Init Serveur
HOST = "192.168.1.4"
PORT = 65432
serveur = Serveur(HOST, PORT)

# Initialisation des composants
bouton = DigitalInOut(board.GP16)
bouton.pull = Pull.DOWN
pot = AnalogIn(board.GP26)

red = DigitalInOut(board.GP19)
red.direction = Direction.OUTPUT
green = DigitalInOut(board.GP20)
green.direction = Direction.OUTPUT
blue = DigitalInOut(board.GP21)
blue.direction = Direction.OUTPUT

# Variables

pressed = False

# limites de valeurs du potentiomètre
# entre réponses 1/2 et 2/3
#thresholds = [22112, 43823]
thresholds = [6500, 59000] #valeurs repoussées pour donner plus de place à l'option 2

# Fonctions

def eteindre():
    red.value = False
    green.value = False
    blue.value = False

def read_reponse():
    reponse = pot.value
    if reponse < thresholds[0]:
        return "R"
    elif reponse < thresholds[1]:
        return "B"
    else:
        return "G"
    
def clignoter(couleur: str):
    timer = 2
    if couleur == "red": led = red
    elif couleur == "green": led = green
    else: led = blue
    
    print("Clignotement")
    while timer > 0:
        led.value = not led.value
        time.sleep(0.1)
        timer -= 0.1
    print("Fin clignotement")
    
# def read_button(pressed)-> bool:
#     if not pressed and bouton.value:
#         print("Pressed")
#         return True
#     elif pressed and not bouton.value:
#         # Action du bouton
#         print("Depressed")
#         read_reponse()
#         return False

## Programme

serveur.Envoyer("Reflexe?")
print("Attente de réponse 'Reflexe=ok'...")
print("Réponse :", serveur.Recevoir())

green.value = True
time.sleep(1)
green.value = False

query = serveur.Recevoir()
if "R" in query:
    red.value = True
elif "G" in query:
    green.value = True
else:
    blue.value = True
    print("Réponse non reconnue :", query)

while not pressed:
    if bouton.value:
        pressed = True
        reponse = read_reponse()
        serveur.Envoyer(reponse)
        print("Réponse envoyée :", reponse)
        print("ACK :", serveur.Recevoir())
        print("Attente de l'annonce du gagnant...")
        print(serveur.Recevoir())
        eteindre()

