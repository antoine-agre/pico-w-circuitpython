import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
from time import sleep
import math

pot = AnalogIn(board.GP26)

ledR = DigitalInOut(board.GP19)
ledR.direction = Direction.OUTPUT
ledG = DigitalInOut(board.GP20)
ledG.direction = Direction.OUTPUT
ledB = DigitalInOut(board.GP21)
ledB.direction = Direction.OUTPUT

MAX_PAUSE = 0.1 #s
MIN_PAUSE = 0.02
# potentiometre à 0% ==> pause de 1s
# potentiometre à 100% ==> pause de 0.01s

def potentiometre_to_pourcent(value):
    return (value - 288) / (65535 - 288)

def value_to_tension(value):
    return value * 3.3

while True:
    #for i in range(3):
    #    values[i] = pots[i].value / 65520
    
    ledR.value = not ledR.value
    
    value = potentiometre_to_pourcent(pot.value)
    pause = MAX_PAUSE - ((MAX_PAUSE - MIN_PAUSE) * value)

    print("pause de", pause, "s")
    sleep(pause)