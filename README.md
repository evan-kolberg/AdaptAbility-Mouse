# What do I need?
## Physical Things ~ Basic Version &darr;
- Arduino UNO
- Joystick 
- 5 male to female wires
- a C2G 5m USB Cable <em>(printer cable)</em>

## Physical Things ~ Advanced Version &darr;
- Everything in the basic version
- 4 buttons
- 4 10k Ω resistors
- 10 male to male wires
- Breadboard with power rails

## Software &darr;
- Arduino IDE
- VS Code <em>(optional, but highly recommended)</em>
- Python 3.8+ (<em>MAKE SURE YOU SELECT <strong>ADD TO PATH</strong></em>)

<hr>

# How do I do this?
1. Connect assemble Arduino as shown in the schematics and plug into your computer
2. Download this repo and open up the folder in VS Code (or any IDE)
3. Edit the COM port number that your Arduino uses in both the .ino and .py files
3. Create a virtual environment <em>~ Explained for VS Code below</em>
4. With that venv active, run: `pip install pyserial pyautogui` in a terminal window
5. Upload the .ino file to the Arduino
6. Run the python file

> If you want more buttons, follow the **Advanced Schematic** and run the files in the **Advanced Folder**

<hr>

<img src="https://user-images.githubusercontent.com/70989484/170832956-d02a45ce-f8e8-459a-8617-57f92748257c.png" alt="Basic" width="50%" height="50%">
<p><em>Basic Schematic ~ Made with Fritzing</em></p>

<hr>

<img src="https://user-images.githubusercontent.com/70989484/170832702-21fbfc89-7145-40fa-8ca1-9a2122772d06.png" alt="Advanced" width="50%" height="50%">
<p><em>Advanced Schematic ~ Made with Fritzing</em></p>

<hr>

<img src="https://user-images.githubusercontent.com/70989484/170808142-f89e6aff-2c69-4d65-9025-2fc2d02f25f6.png" alt="Real" width="50%" height="50%">
<p><em>Advanced Schematic ~ Made in real life</em></p>

<hr>

# How to Create a Virtual Environment for Python in VS Code
## Always start with a project folder (download this repo to use as one)

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
