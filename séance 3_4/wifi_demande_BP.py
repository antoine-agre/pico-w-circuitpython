from Serveur import Serveur
import time
import board
from digitalio import DigitalInOut, Pull
from analogio import AnalogIn

# Init Serveur
HOST = "192.168.1.11"
PORT = 65001
serveur = Serveur(HOST, PORT)

# Initialisation du bouton poussoir
bouton = DigitalInOut(board.GP16)
bouton.pull = Pull.DOWN
pot = AnalogIn(board.GP26)

demandes = ["Pot?min", "Pot?max", "Pot?avg"]

nombre_de_lectures = 0
dernier_appui = 0
compteur_appuis = 0


while True:
    if bouton.value: # Note: "not bouton.value" signifie que le bouton est pressé si le bouton est configuré en pull-down
        time_bouton_presse = time.monotonic()
        
        # Attendre la libération du bouton
        while bouton.value:
            time.sleep(0.01)
        
        temps_appui = time.monotonic() - time_bouton_presse
        
        # Vérifier si c'était une longue pression
        if temps_appui > 3:
            serveur.Envoyer("Pot=" + str(pot.value))
            print("Réponse à envoi :", serveur.Recevoir())
            compteur_appuis = 0 # Réinitialiser le compteur d'appuis
        else:
            # C'est une pression courte
            if time.monotonic() - dernier_appui < 0.5:
                compteur_appuis += 1
            else:
                compteur_appuis = 1
            
            dernier_appui = time.monotonic()
            
            if compteur_appuis == 1:
                serveur.Envoyer(demandes[0])
                print("Réponse à", demandes[0], ":", serveur.Recevoir())
            elif compteur_appuis == 2:
                serveur.Envoyer(demandes[1])
                print("Réponse à", demandes[1], ":", serveur.Recevoir())
            elif compteur_appuis == 3:
                serveur.Envoyer(demandes[2])
                print("Réponse à", demandes[2], ":", serveur.Recevoir())
                compteur_appuis = 0 # R√©initialiser le compteur apr√®s avoir trait√© un triple appui
        
        nombre_de_lectures += 1
    
    time.sleep(0.1)





    #######


    
    
################
    



