from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut

#red = DigitalInOut(board.GP11)
red = AnalogOut(board.GP26)
red.direction = Direction.OUTPUT
#green = DigitalInOut(board.GP12)
red = AnalogOut(board.GP27)
green.direction = Direction.OUTPUT
#blue = DigitalInOut(board.GP13)
red = AnalogOut(board.GP28)
blue.direction = Direction.OUTPUT

red.value = 0.5

red.value = 0.1

# cycle chaque couleur primaire pendant 3 secondes
# while True:
#     for led in leds:
#         led.value = False
#     leds[index].value = True
#     
#     sleep(3)
#     
#     index = (index + 1) % 3