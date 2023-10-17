import time
import os
import ssl
import wifi
import socketpool
import microcontroller
import adafruit_requests

# Configuration du serveur
ADRESSE_IP_DU_SERVEUR = "192.168.1.100"
PORT_DU_SERVEUR = "8000"

# Connexion au réseau Wi-Fi
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

# Construction de l'URL pour interroger le serveur
url = "http://" + ADRESSE_IP_DU_SERVEUR + ":" + PORT_DU_SERVEUR + "/fichier?bibliotheques.json"
print(url)

# Création d'une session pour envoyer des requêtes
pool = socketpool.SocketPool(wifi.radio)
session_requete = adafruit_requests.Session(pool, ssl.create_default_context())

try:
    # Envoi d'une requête au serveur et récupération de la réponse
    reponse = session_requete.get(url)
    
    # Conversion de la réponse en format JSON
    reponse_en_json = reponse.json()
    
    # Affichage de la réponse
    print()
    print(reponse_en_json)
    print()
    print(reponse_en_json['bibliotheque']['localisation'])
    print()
    print(reponse_en_json['bibliotheque']['livres'])
    print()
    
    # Affichage des livres de la bibliothèque
    liste_des_livres = reponse_en_json['bibliotheque']['livres']
    for livre in liste_des_livres:
        print(f"{livre['titre']}, de {livre['auteur']}")

# Gestion des erreurs potentielles lors de la requête
except Exception as e:
    print("Erreur :\n", str(e))
    print("Redémarrage du microcontrôleur dans 10 secondes")
    time.sleep(10)
    microcontroller.reset()
