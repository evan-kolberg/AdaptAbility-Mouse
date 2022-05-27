from serial import Serial
from pyautogui import moveTo

s = Serial('COM5', '9600')

'''Since 0,0 is in the top left corner of
the screen in pyautogui, we have to
subtract y from the max screen height'''

# each line comes in as "x y"
# split to separate them
# then send mouse to those coordinates
while True:
    read = s.readline().decode('ASCII')
    values = read.split()
    moveTo(int(values[0]), 1439-int(values[1]), 0.01)
close()