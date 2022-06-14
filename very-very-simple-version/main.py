from serial import Serial
import pyautogui
from threading import Thread
from time import sleep

# prevents the program from stopping after touching a corner
pyautogui.FAILSAFE = False

connected = False

while not connected:
    try:
        # edit serial port
        s = Serial('COM5', '9600')
        # if the program has a bad start (like, a decoding error) then try again
        s.readline().decode('utf-8').split()
        connected = True
        print('\nConnection Successful')
    except UnicodeDecodeError:
        pass

# parameters for how the program operates
deadzone = 20
butter = 35
delay = 0.15

cooldowns = {'joystick': 'ready'}
previous1 = 0


# deataches from main program so it doesn't get slowed down
def cool(clicky_thing):
    sleep(delay)
    cooldowns[clicky_thing] = 'ready'

while True:
    try:
        values = s.readline().decode('utf-8').split()
        # A0 A1 8 12 11 10 9
        # vrx vry sw button1 button2 button3 button4
        x = int(values[0])-511.5
        y = int(values[1])-511.5
        joystick_click = int(values[2])

        # slows the movements of the mouse cursor
        vx = x/butter
        vy = y/butter

        # joystick click uses an internal pullup resistor ~ will show 0 when clicked
        if previous1 == 1 and joystick_click == 0:
            if cooldowns['joystick'] == 'ready':
                thread = Thread(target=pyautogui.mouseDown)
                thread.start()
                cooldowns['joystick'] = 'waiting'
                thread = Thread(target=cool, args=['joystick'])
                thread.start()
        elif previous1 == 0 and joystick_click == 1:
            thread = Thread(target=pyautogui.mouseUp)
            thread.start()
        
        previous1 = joystick_click

        if x < deadzone*-1 or x > deadzone or y < deadzone*-1 or y > deadzone:
            thread = Thread(target=pyautogui.moveRel, args=(vx, vy))
            thread.start()

    except KeyboardInterrupt:    # CTRL + C
        s.close()
        print('\nSerial Monitor closed')
        break
