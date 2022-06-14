from serial import Serial
import pyautogui
from threading import Thread
from time import sleep

pyautogui.FAILSAFE = False

connected = False

while not connected:
    try:
        # edit serial port
        s = Serial('COM5', '9600')
        s.readline().decode('utf-8').split()
        connected = True
        print('\nConnection Successful')
    except UnicodeDecodeError:
        pass


deadzone = 20
butter = 50
delay = 0.15

up_down = 'up'
cooldowns = {'joystick': 'ready'}


def jsc():
    pyautogui.click(button='middle')

def move(vx, vy):
    pyautogui.moveRel(vx, vy)

def cool(clicky_thing):
    sleep(delay)
    cooldowns[clicky_thing] = 'ready'
        

while True:
    try:
        values = s.readline().decode('utf-8').split()
        x = int(values[0])-511.5
        y = int(values[1])-511.5
        joystick_click = int(values[2])

        vx = x/butter
        vy = y/butter

        # joystick click uses an internal pullup resistor ~ will show 0 when clicked
        if joystick_click == 0:
            if cooldowns['joystick'] == 'ready':
                thread = Thread(target=jsc)
                thread.start()
                cooldowns['joystick'] = 'waiting'
                thread = Thread(target=cool, args=['joystick'])
                thread.start()

        if x < deadzone*-1 or x > deadzone or y < deadzone*-1 or y > deadzone:
            thread = Thread(target=move, args=(vx, vy))
            thread.start()

    except KeyboardInterrupt:
        s.close()
        print('\nSerial Monitor closed')
        break
