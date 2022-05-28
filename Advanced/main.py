from serial import Serial
from pyautogui import moveRel, click, mouseUp, mouseDown

s = Serial('COM5', '9600')


deadzone = 20
butter = 20


while True:
    try:
        values = s.readline().decode('utf-8').split()
        x = int(values[0])-511.5
        y = int(values[1])-511.5
        joystick_click = int(values[2])
        button1 = int(values[3])
        button2 = int(values[4])
        button3 = int(values[5])
        button4 = int(values[6])


        vx = x/butter
        vy = y/butter

        print(f'x: {x}' + ' '*(15-len(str(x))) + f'y: {y}' + ' '*(15-len(str(y))) + f'vx: {vx}' + ' '*(15-len(str(vx))) + f'vy: {vy}' + ' '*(15-len(str(vy))), values)

        # joystick click uses an internal pullup resistor
        if joystick_click == 0:
            click(button='left')

        # buttons use external resistors
        if button1 == 1:
            click(button='left')

        if button2 == 1:
            click(button='right')

        if button3 == 1:
            mouseDown()

        if button4 == 1:
            mouseUp()



        if x < deadzone*-1 or x > deadzone or y < deadzone*-1 or y > deadzone:
            moveRel(vx, vy)

    except KeyboardInterrupt:
        s.close()
        print('Serial Monitor closed')
        break
