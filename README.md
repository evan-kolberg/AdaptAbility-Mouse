# What you need
| Physical Things &darr; | 
| ----------- |
- Arduino UNO
- Joystick
- 5 male to female wires
- a C2G 5m USB Cable <em>(printer cable)</em>

| Software &darr; | 
| ----------- |
- Arduino IDE
- VS Code <em>(optional, but highly recommended)</em>
- Python 3.8+ <em>MAKE SURE YOU SELECT <strong>ADD TO PATH</strong></em>

<br><br>
# Steps
1. Connect Arduino to joystick as shown in the schematic and plug into your computer
2. Download this repo and open up the folder in VS Code (or any IDE)
3. Edit the COM port number that your Arduino uses in both the .ino and .py files
3. Create a virtual environment <em>~ Explained for VS Code below</em>
4. With that venv active, run: `pip install pyautogui` in a terminal window
5. Upload the .ino file to the Arduino
6. Run the python file 

<br><br>


<figure>
    <img src="https://user-images.githubusercontent.com/70989484/170765960-ed97007c-c077-4ef1-b973-cbaa6cafd654.png"
         alt="Schematic">
    <figcaption><center><em>Schematic made with Fritzing</em></center></figcaption>
</figure>


<br><br>

# How to Create a Virtual Environment for Python in VS Code
## Always start with a project folder (download this repo to use as one)

Start by clicking 'New Terminal' under the  'Terminal' section on the top left part of VS Code.

Windows &darr;
- CMD  -->  `python -m venv venv`
- Powershell --> `py -m venv venv`
> **Note:** If you're using powershell, know that Microsoft makes you use `py` to reference the default installation of python. Otherwise, you will get a pop-up to the Windows Store, begging you to download their unstable version. Obviously, don't do what they're asking you to and stick with your installation.

macOS &darr;
- ZSH --> `python3 -m venv venv`

Next step for both OS types &darr;

- Do **CRTL + SHFT + P**  &rarr;  Type in 'Python: Select Interpreter' and hit enter. From there, click on the option with a star next to it. If there isn't a star next to any of them, look for .venv\Scripts\python.exe in your project folder. If there isn't a venv folder, then troubleshoot on the internet.
- Do **CTRL + SHFT + `**  &rarr;  This should run the 'activate' file in the folder of the selected interpreter and pop-up with a terminal that says ``(venv)`` We know that the venv is working because it says '(venv)' before the project folder. From here, you can install libraries using pip without touching your main installation of python.
