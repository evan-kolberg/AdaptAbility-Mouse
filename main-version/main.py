from serial import Serial
import pyautogui
from threading import Thread
from time import sleep

# prevents the program from stopping after touching a corner
pyautogui.FAILSAFE = False

connected = False

while not connected:
    try:
        # ------ EDIT SERIAL PORT HERE ------
        s = Serial('COM5', '9600')
        # if the program has a bad start (like, a decoding error) then try again
        s.readline().decode('utf-8').split()
        connected = True
        print('\nConnection Successful')
    except (UnicodeDecodeError, ValueError):
        pass

# parameters for how the program operates
deadzone = 20
butter = 35
delay = 0.15

# don't touch these
cooldowns = {'joystick': 'ready', 'b1': 'ready', 'b2': 'ready'}
previous1 = 0
previous2 = 0
oldPos = 0

# detaches from main program so it doesn't get slowed down
def cool(clicky_thing):
    sleep(delay)
    cooldowns[clicky_thing] = 'ready'

while True:
    try:
        values = s.readline().decode('utf-8').split()
        # A0 A1 8 12 11
        # vrx vry sw button1 button2
        x = int(values[0])-511.5
        y = int(values[1])-511.5
        joystick_click = int(values[2])
        
        b1 = int(values[3])
        b2 = int(values[4])

        # TURN KNOB VERY SLOWLY
        enc = int(values[5])
        # slows the movements of the mouse cursor
        vx = x/butter
        vy = y/butter

        # joystick click uses an internal pullup resistor ~ will show 0 when clicked
        if joystick_click == 0:    # if clicked
            if cooldowns['joystick'] == 'ready':    # # excecutes function if ready
                thread = Thread(target=pyautogui.click, kwargs={'button': 'middle'})
                thread.start()
                cooldowns['joystick'] = 'waiting'
                thread = Thread(target=cool, args=['joystick'])    # triggers cooldown
                thread.start()

        # buttons use external resistors ~ will show 1 when clicked
        if previous1 == 0 and b1 == 1:
            if cooldowns['b1'] == 'ready':
                thread = Thread(target=pyautogui.mouseDown)
                thread.start()
                cooldowns['b1'] = 'waiting'
                thread = Thread(target=cool, args=['b1'])    # triggers cooldown
                thread.start()
        elif previous1 == 1 and b1 == 0:
            thread = Thread(target=pyautogui.mouseUp)
            thread.start()
        
        previous1 = b1

        if previous2 == 0 and b2 == 1:
            if cooldowns['b2'] == 'ready':
                thread = Thread(target=pyautogui.click, kwargs={'button': 'right'})
                thread.start()
                cooldowns['b2'] = 'waiting'
                thread = Thread(target=cool, args=['b2'])    # triggers cooldown
                thread.start()
        
        previous2 = b2

        if x < deadzone*-1 or x > deadzone or y < deadzone*-1 or y > deadzone:
            thread = Thread(target=pyautogui.moveRel, args=(vx, vy))
            thread.start()

        # TURN KNOB VERY SLOWLY
        newPos = enc
        if newPos != oldPos:
            thread = Thread(target=pyautogui.scroll, args=[(newPos-oldPos)*-50])
            thread.start()
        oldPos = newPos

    except KeyboardInterrupt:    # CTRL + C
        s.close()
        print('\nSerial Monitor closed')
        break
