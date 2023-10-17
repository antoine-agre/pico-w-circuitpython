from Serveur import Serveur

HOST = "192.168.1.11"
PORT = 65001

serveur = Serveur(HOST, PORT)

# Seulement après avoir envoyé des valeurs !
demandes = ["Pot?min", "Pot?max", "Pot?avg"]

for demande in demandes:

    serveur.Envoyer(demande)
    print("Réponse à", demande, ":", serveur.Recevoir())