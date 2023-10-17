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

def pourcent(value):
    return (value - 288) / (65535 - 288)

def value_to_tension(value):
    return value * 3.3

while True:
    #for i in range(3):
    #    values[i] = pots[i].value / 65520
    
    value = pot.value / (65520/8)
    value = math.floor(value)
    if value == 8: value = 7
    # 0 - 7

    ledR.value = (value % 2 == 1)
    ledG.value = (value in [2, 3, 6, 7])
    ledB.value = (value >= 4)

    print(value)
    print(pot.value)
    print(":", pourcent(pot.value))
    print("tension :", value_to_tension(pourcent(pot.value)), "V")
    sleep(0.1)