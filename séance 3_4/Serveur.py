
      
import wifi
import socketpool
import ssl
import time
import os
import ipaddress
TIMEOUT = None



class Serveur:
    def __init__(self, ip, port) :
        self.socket = None
        self.ip = ip
        self.port = port
        self.messageRecu =""
        #print("dd")
        self.Connection()

    def Connection(self):
        print("Tentative de connection au WiFi de SSID ",os.getenv('CIRCUITPY_WIFI_SSID'))
        #  connect to your SSID
        wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
        print("Connecté au WiFi")
        pool = socketpool.SocketPool(wifi.radio)
        print("Creation de la socket")
        #with pool.socket(pool.AF_INET, pool.SOCK_STREAM) as s:
        self.socket = pool.socket(pool.AF_INET, pool.SOCK_STREAM) 
        self.socket.settimeout(TIMEOUT)
        print("Connection au serveur")
        self.socket.connect((self.ip, self.port))        

    def Envoyer(self,message):
        #print("Envoi")
        message = str(message)
        message = message.encode('utf-8')
        #print(message)
        envoi = self.socket.send(message)
        self.messageRecu =""
        #self.RecevoirApresEnvoyer()
        
    
    def Recevoir(self):
        #print("Reception")
        buff = bytearray(128)
        numbytes = self.socket.recv_into(buff)
        self.messageRecu = buff.decode('utf-8')
        return self.messageRecu

    
 
      

