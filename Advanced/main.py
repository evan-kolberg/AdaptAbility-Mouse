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
delay = 0.20

up_down = 'up'
cooldowns = {'joystick': 'ready', 'b1': 'ready', 'b2': 'ready', 'b3': 'ready', 'b4': 'ready'}

# functions that excecute and detatch after ran
def jsc():
    pyautogui.click(button='middle')

def move(vx, vy):
    pyautogui.moveRel(vx, vy)

def cool(clicky_thing):
    sleep(delay)
    cooldowns[clicky_thing] = 'ready'

def b1():
    pyautogui.click(button='primary')

def b2():
    pyautogui.click(button='secondary')

def b3():
    global up_down
    if up_down == 'up':
        pyautogui.mouseDown()
        up_down = 'down'
    else:
        pyautogui.mouseUp()
        up_down = 'up'

def b4():
    pyautogui.scroll(-15)


while True:
    try:
        values = s.readline().decode('utf-8').split()
        # A0 A1 8 12 11 10 9
        # vrx vry sw button1 button2 button3 button4
        x = int(values[0])-511.5
        y = int(values[1])-511.5
        joystick_click = int(values[2])

        buttonStates = [int(values[3]), int(values[4]), int(values[5]), int(values[6])]
        buttonFunctions = {'b1': b1, 'b2': b2, 'b3': b3, 'b4': b4}

        # slows the movements of the mouse cursor
        vx = x/butter
        vy = y/butter

        # joystick click uses an internal pullup resistor ~ will show 0 when clicked
        if joystick_click == 0:    # if clicked
            if cooldowns['joystick'] == 'ready':    # # excecutes function if ready
                thread = Thread(target=jsc)
                thread.start()
                cooldowns['joystick'] = 'waiting'
                thread = Thread(target=cool, args=['joystick'])    # triggers cooldown
                thread.start()

        # buttons use external resistors ~ will show 1 when clicked
        for i in range(4):    # repeat for the 4 buttons
            if buttonStates[i] == 1:    # if clicked
                name = f'b{i+1}'
                if cooldowns[name] == 'ready':    # excecutes function if ready
                    thread = Thread(target=buttonFunctions[name])
                    thread.start()
                    cooldowns[name] = 'waiting'
                    thread = Thread(target=cool, args=[name])    # triggers cooldown
                    thread.start()
        
        if x < deadzone*-1 or x > deadzone or y < deadzone*-1 or y > deadzone:
            thread = Thread(target=move, args=(vx, vy))
            thread.start()

    except KeyboardInterrupt:    # CTRL + C
        s.close()
        print('\nSerial Monitor closed')
        break
