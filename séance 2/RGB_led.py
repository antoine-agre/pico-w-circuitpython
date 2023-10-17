from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull

red = DigitalInOut(board.GP11)
red.direction = Direction.OUTPUT
green = DigitalInOut(board.GP12)
green.direction = Direction.OUTPUT
blue = DigitalInOut(board.GP13)
blue.direction = Direction.OUTPUT

# cathode commune
red.value = False
green.value = False
blue.value = True

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = False
