from time import sleep
from time import sleep, monotonic
import board
from digitalio import DigitalInOut, Direction, Pull

button = DigitalInOut(board.GP13)
button.pull = Pull.DOWN #pull implique INPUT
led = DigitalInOut(board.GP14)
led.direction = Direction.OUTPUT

# while True:
#     led.value = button.value

is_button_held = False
time_left = 0
current_time = monotonic()

def button_pressed():
    global time_left
    time_left += 5
    print("Temps Restant : ", time_left)

def button_released():
    pass

while True:
    
    # Calcul du temps
    
    new_time = monotonic()
    delta = new_time - current_time
    current_time = new_time
    #comparer floor pour savoir si on vient de passer une seconde, et print Xs restantes
    
    time_left = max(0, time_left - delta)
    
    # Logique du bouton
    
    if button.value == True:
        if not is_button_held:
            print("bouton appuyé")
            is_button_held = True
            button_pressed()
                        
    else:
        if is_button_held:
            print("bouton relaché")
            is_button_held = False
            button_released()
            
    # Contrôle de la LED
    
    if led.value:
        if time_left == 0:
            led.value = False
    else:
        if time_left > 0:
            led.value = True

    # Sleep

    sleep(0.01)
