from Serveur import Serveur
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
from time import sleep
import math

HOST = "192.168.1.11"
PORT = 65001
serveur = Serveur(HOST, PORT)

pot = AnalogIn(board.GP26)



for _ in range(20):

    serveur.Envoyer("Pot=" + str(pot.value))
    print("Réponse à envoi :", serveur.Recevoir())
    sleep(0.2)