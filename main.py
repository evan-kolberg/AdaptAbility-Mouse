from serial import Serial
from pyautogui import moveRel, click, mouseUp, mouseDown, scroll
import threading

s = Serial('COM5', '9600')


deadzone = 20
butter = 20

jsc = lambda: click(button='primary')
move = lambda vx, vy: moveRel(vx, vy)


while True:
    try:
        values = s.readline().decode('utf-8').split()
        x = int(values[0])-511.5
        y = int(values[1])-511.5
        joystick_click = int(values[2])

        vx = x/butter
        vy = y/butter

        print(f'x: {x}' + ' '*(15-len(str(x))) + f'y: {y}' + ' '*(15-len(str(y))) + f'vx: {vx}' + ' '*(15-len(str(vx))) + f'vy: {vy}' + ' '*(15-len(str(vy))), values)

        # joystick click uses an internal pullup resistor
        if joystick_click == 0:
            thread = threading.Thread(target=jsc)
            thread.start()            

        if x < deadzone*-1 or x > deadzone or y < deadzone*-1 or y > deadzone:
            thread = threading.Thread(target=move, args=(vx, vy))
            thread.start()

    except KeyboardInterrupt:
        s.close()
        print('Serial Monitor closed')
        break
