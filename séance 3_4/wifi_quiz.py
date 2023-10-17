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

# limites de valeurs du potentiomètre
# entre réponses 1/2 et 2/3
#thresholds = [22112, 43823]
thresholds = [15000, 50000] #valeurs repoussées pour donner plus de place à l'option 2

def eteindre():
    red.value = False
    green.value = False
    blue.value = False

def read_reponse():
    reponse = pot.value
    if reponse < thresholds[0]:
        return 1
    elif reponse < thresholds[1]:
        return 2
    else:
        return 3
    
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


print("Envoi : 'Quiz?'")
serveur.Envoyer("Quizz?")
print("Réponse :")
print(serveur.Recevoir())

while True:
    
    # Bouton
    if bouton.value is True and pressed is False:
        pressed = True
    elif bouton.value is False and pressed is True:
        pressed = False
        print("Envoi :", read_reponse())
        serveur.Envoyer(read_reponse())
        print("Réponse :")
        reponse = serveur.Recevoir()
        print(reponse)
        if "Correct" in reponse:
            clignoter("green")
        else:
            clignoter("red")

        print("\n",serveur.Recevoir())
    time.sleep(0.01)
#     if bouton.value and pressed == False:
#         pressed = True
#         serveur.Envoyer("RGB?")
#         reponse = serveur.Recevoir()
#         eteindre()
#         print("Réponse :", reponse)
#         if 'R' in reponse:
#             red.value = True
#         elif 'G' in reponse:            
#             green.value = True
#         elif 'B' in reponse:
#             blue.value = True
#         else:
#             print("Réponse erronée.")
#     elif not bouton.value and pressed:
#         pressed = False

