from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull

red = DigitalInOut(board.GP11)
red.direction = Direction.OUTPUT
green = DigitalInOut(board.GP12)
green.direction = Direction.OUTPUT
blue = DigitalInOut(board.GP13)
blue.direction = Direction.OUTPUT

leds = [red, green, blue]
for led in leds:
    led.value = False

index = 0

# cycle chaque couleur primaire pendant 3 secondes
while True:
    for led in leds:
        led.value = False
    leds[index].value = True
    
    sleep(3)
    
    index = (index + 1) % 3