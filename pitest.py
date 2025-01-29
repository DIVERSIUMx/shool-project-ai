from gpiozero import LED, Button
from time import sleep
from signal import pause

from scanner import check
from cam import shot


green = LED(4)
yellow = LED(3)
red = LED(2)

button = Button(14)
button.hold_time = 0.2

green.off()
yellow.off()
red.off()

def nothing():
    pass

def press(): 
    try:
        button.when_pressed = nothing
        yellow.on()
        print("hellp")
        shot()
        if check():
            green.on()
        else:
            red.on()
        yellow.off()
        sleep(2)
        green.off()
        red.off()

        button.when_held = press
    except:
        button.when_held = press
        green.off()
        yellow.off()
        red.off()
        return


button.when_pressed = press


pause()

#while True:
 #   red.off()
#    green.on()
#    sleep(1)
#    green.off()
#    yellow.on()
#    sleep(1)
#    yellow.off()
#    red.on()
#    sleep(1)
