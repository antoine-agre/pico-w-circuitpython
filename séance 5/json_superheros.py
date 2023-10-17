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
url = "http://" + ADRESSE_IP_DU_SERVEUR + ":" + PORT_DU_SERVEUR + "/fichier?superheros-light.json"
print(url)

# Création d'une session pour envoyer des requêtes
pool = socketpool.SocketPool(wifi.radio)
session_requete = adafruit_requests.Session(pool, ssl.create_default_context())

def afficher_details(id):
    hero = dict_superheros[id]
    stats = hero['powerstats']
    look = hero['appearance']
    print()
    print(f"Nom du super-héros : {hero['name']}")
    print("-------------------------------------")
    print(f"Intelligence : {stats['intelligence']}")
    print(f"Force : {stats['strength']}")
    print(f"Vitesse : {stats['speed']}")
    print(f"Résistance : {stats['durability']}")
    print(f"Taille : {look['height'][1]}")
    print(f"Poids : {look['weight'][1]}")
    print(f"Couleur des yeux : {look['eyeColor']}")
    print(f"Couleur des cheveux : {look['hairColor']}")
    print()

try:
    # Envoi d'une requête au serveur et récupération de la réponse
    reponse = session_requete.get(url)
    
    # Conversion de la réponse en format JSON
    reponse_en_json = reponse.json()
    
    # Organiser les données dans un dictionnaire pour un accès facile
    dict_superheros = {}
    for superhero in reponse_en_json:
        id = superhero['id']
        dict_superheros[id] = superhero

    # Afficher les ID des super-héros
    for id in dict_superheros:
        print(id)
        
    # Accéder aux détails d'un élément spécifique par ID
    id_a_chercher = 1
    if id_a_chercher in dict_superheros:
        print(dict_superheros[id_a_chercher]['name'])
    else:
        print(f"Aucun super-héros trouvé avec l'ID {id_a_chercher}")

    # Affichage de tous les héros préfixé de leur ID
    print()
    for id in dict_superheros:
        print(f"[{id}] {dict_superheros[id]['name']}")
    
    # Affichage des détails
    afficher_details(2)
        
    # Affichage des pouvoirs d'un héros par entrée utilisateur
    input_id = int(input("Identifiant ? "))
    afficher_details(input_id)

# Gestion des erreurs potentielles lors de la requête
except Exception as e:
    print("Erreur :\n", str(e))
    print("Redémarrage du microcontrôleur dans 10 secondes")
    time.sleep(10)
    microcontroller.reset()
