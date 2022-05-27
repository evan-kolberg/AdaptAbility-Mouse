from serial import Serial
from pyautogui import moveRel

s = Serial('COM5', '9600')


'''0,0 is in the top left corner of
the screen in pyautogui'''

'''
    # very fast, innacurate, and tedious ~ only for 4k
    C++:
        int x = map(analogRead(A1), 0, 1023, 2559, 0); 
        int y = map(analogRead(A0), 0, 1023, 0, 1439);
    Python:
        moveTo(x, y, 0.01)
'''

'''
each line comes in as "x y"
split to separate them
then send mouse to those coordinates
'''


while True:
    values = s.readline().decode('utf-8').split()
    x = int(values[0])
    y = int(values[1])
    print(f'X: {x}' + ' '*(6-len(str(x))) + f'Y: {y}')
    

    # smoother option for any screen display
    deadzone = 20
    slow = 10

    vx = x/slow
    vy = y/slow

    if vx > deadzone*-1 and vx < deadzone:
        if vy > deadzone*-1 and vy < deadzone:
            continue

    moveRel(vx, vy*-1)
