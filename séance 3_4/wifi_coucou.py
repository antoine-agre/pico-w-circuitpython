from Serveur import Serveur

HOST = "192.168.1.4"
PORT = 65000

serveur = Serveur(HOST, PORT)

serveur.Envoyer("coucou")
print("Réponse du serveur :", serveur.Recevoir())

serveur.Envoyer("coucou")
print("Réponse du serveur :", serveur.Recevoir())