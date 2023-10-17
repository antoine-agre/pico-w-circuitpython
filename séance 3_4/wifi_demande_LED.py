from Serveur import Serveur
import time
import board
from digitalio import DigitalInOut, Pull, Direction
from analogio import AnalogIn

# Init Serveur
HOST = "192.168.1.4"
PORT = 65000
serveur = Serveur(HOST, PORT)

# Initialisation du bouton poussoir
bouton = DigitalInOut(board.GP16)
bouton.pull = Pull.DOWN
pot = AnalogIn(board.GP26)

red = DigitalInOut(board.GP19)
red.direction = Direction.OUTPUT
green = DigitalInOut(board.GP20)
green.direction = Direction.OUTPUT
blue = DigitalInOut(board.GP21)
blue.direction = Direction.OUTPUT

pressed = False

def eteindre():
    red.value = False
    green.value = False
    blue.value = False

while True:
    if bouton.value and pressed == False:
        pressed = True
        serveur.Envoyer("RGB?")
        reponse = serveur.Recevoir()
        eteindre()
        print("Réponse :", reponse)
        time.sleep(0.1)
        if 'R' in reponse:
            red.value = True
        elif 'G' in reponse:            
            green.value = True
        elif 'B' in reponse:
            blue.value = True
        else:
            print("Réponse erronée.")
    elif not bouton.value and pressed:
        pressed = False
    time.sleep(0.01)

