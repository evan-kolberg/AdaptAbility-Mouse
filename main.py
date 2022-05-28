from serial import Serial
from pyautogui import moveRel, click

s = Serial('COM5', '9600')


'''
0,0 is in the top left corner of
the screen in pyautogui

each line comes in as "x y"
split to separate them
then send mouse to those coordinates
'''

deadzone = 20
butter = 20

while True:
    try:
        values = s.readline().decode('utf-8').split()
        x = int(values[0])-511.5
        y = int(values[1])-511.5
        pin_8 = int(values[2])

        vx = x/butter
        vy = y/butter

        print(f'x: {x}' + ' '*(20-len(str(x))) + f'y: {y}' + ' '*(20-len(str(y))) + f'vx: {vx}' + ' '*(20-len(str(vx))) + f'vy: {vy}' + ' '*(20-len(str(vy))), values)

        if pin_8 == 0:
            click(button='left')

        if x < deadzone*-1 or x > deadzone or y < deadzone*-1 or y > deadzone:
            moveRel(vx, vy)

    except KeyboardInterrupt:
        s.close()
        print('Serial Monitor closed')
        break
