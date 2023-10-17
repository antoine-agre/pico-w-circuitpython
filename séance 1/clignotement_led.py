from time import sleep
import board
from digitalio import DigitalInOut, Direction

# La LED qui se trouve sur la carte
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

duration = float(input("Durée d'un clignotement (s) : "))
blink_amount = int(input("Nombre de clignotements (0 = infini) : "))

def blink():
    led.value = True
    print("led on : allumée")
    sleep(duration/2)
    
    led.value = False
    print("led off : éteinte")
    sleep(duration/2)

if blink_amount == 0:
    while True:
        blink()
else:
    for i in range(blink_amount):
        blink()
    print("Clignotements finis.")
