# ULTIMATE WALMART GAMING MOUSE
## What do I need?
### Physical Things ~ Simple Version &darr;
- Arduino UNO
- Joystick 
- 5 male to female wires
- a USB AB cable <em>(printer cable)</em>

### Physical Things ~ Main Version &darr;
- Arduino UNO
- Joystick
- 2 buttons
- I2C LCD Display
- Rotary encoder
- RGB LED
- Breadboard
- 2 10k Ω resistors
- 3 220 Ω resistors
- a LOT of male to male cables
- a LOT of male to female cables
- a USB AB cable <em>(printer cable)</em>

### Software &darr;
- Arduino IDE
- VS Code <em>(optional, but highly recommended)</em>
- Python 3.8+ (<em>MAKE SURE YOU SELECT <strong>ADD TO PATH</strong></em>)

<hr>

## How do I do this?
1. Choose a path: Main Version (cool) or Simple Verion (not cool) and downolad this repo
2. If you choose the Main Version, go ahead and look at the .ino file to see how to assemble the hardware with the correct pin formation.
3. Edit the COM port number in the python file that matches the COM port that your Arduino runs on (check using the Arduino IDE)
4. Create a virtual environment in Python <em>~ Explained for VS Code below</em>
5. Install the dependencies with `pip install pyserial pyautogui` in a terminal window (preferably in the virtual env)
6. Upload the .ino file to the Arduino 
7. Run the python file

<hr>

<img src="https://user-images.githubusercontent.com/70989484/173990813-af626dca-5e85-4971-926e-b44828880996.png" alt="Advanced" width="50%" height="50%">
<p><em>Main Version ~ Not Made with Fritzing</em></p>

<hr>

<img src="https://user-images.githubusercontent.com/70989484/170832956-d02a45ce-f8e8-459a-8617-57f92748257c.png" alt="Basic" width="50%" height="50%">
<p><em>Simple Version ~ Made with Fritzing</em></p>
<hr>

## How to Create a Virtual Environment for Python in VS Code
### Always start with a project folder (download this repo to use as one)

Start by clicking 'New Terminal' under the  'Terminal' section on the top left part of VS Code.

Windows &darr;
- CMD  -->  `python -m venv venv`
- Powershell --> `py -m venv venv`
> **Note:** If you're using powershell, know that Microsoft makes you use `py` to reference the default installation of python. Otherwise, you will get a pop-up to the Windows Store, begging you to download their unstable version. Obviously, don't do what they're asking you to and stick with your installation.
- Do **CRTL + SHFT + P**  &rarr;  Type in 'Python: Select Interpreter' and hit enter. From there, click on the option with a star next to it. If there isn't a star next to any of them, look for .venv\Scripts\python.exe in your project folder. If there isn't a venv folder, then troubleshoot on the internet.
- Do **CTRL + SHFT + \`**  &rarr;  This should run the 'activate' file in the folder of the selected interpreter and pop-up with a terminal that says ``(venv)`` We know that the venv is working because it says '(venv)' before the project folder. From here, you can install libraries using pip without touching your main installation of python.

macOS &darr;
- ZSH --> `python3 -m venv venv`
- Do **CMND + SHFT + P**  &rarr;  Type in 'Python: Select Interpreter' and hit enter. From there, click on the option with a star next to it. If there isn't a star next to any of them, look for .venv\Scripts\python.exe in your project folder. If there isn't a venv folder, then troubleshoot on the internet.
- Do **CTRL + SHFT + \`**  &rarr;  This should run the 'activate' file in the folder of the selected interpreter and pop-up with a terminal that says ``(venv)`` We know that the venv is working because it says '(venv)' before the project folder. From here, you can install libraries using pip without touching your main installation of python.
<hr>
