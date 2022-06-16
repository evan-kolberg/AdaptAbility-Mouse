#include <LiquidCrystal_I2C.h>
#include <Wire.h>

// Pins for the hardware
int inputCLK = 5;  // Rotary encoder CLK
int inputDT = 6;  // Rotary encoder DT
const int vrx = A0;  // Joystick VRX
const int vry = A1;  // Joystick VRY
const int sw = 7;  // Joystick SW
const int button1 = 12;  // Button Activation
const int button2 = 11;  // Button Activation
const int red = 10; // Red pin on RGB LED
const int green = 9;  // Green pin on RGB LED
const int blue = 8;  // Blue pin on RGB LED
int counter = 0;
int currentStateCLK;
int previousStateCLK;
int r = 255;
int g = 0;
int b = 0;

LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  pinMode(sw, INPUT_PULLUP);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(inputCLK, INPUT);
  pinMode(inputDT, INPUT);

  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("U SUCK LOL");

  previousStateCLK = digitalRead(inputCLK);
}

void loop() {
  Serial.print(analogRead(vrx));
  Serial.print(' ');
  Serial.print(analogRead(vry));
  Serial.print(' ');
  Serial.print(digitalRead(sw));
  Serial.print(' ');
  Serial.print(digitalRead(button1));
  Serial.print(' ');
  Serial.print(digitalRead(button2));
  Serial.print(' ');

  analogWrite(red, r);
  analogWrite(green, g);
  analogWrite(blue, b);

  currentStateCLK = digitalRead(inputCLK);
  // TURN KNOB VERY SLOWLY
  if (currentStateCLK != previousStateCLK) {
    // the encoder is rotating counterclockwise
    if (digitalRead(inputDT) != currentStateCLK) {
      counter--;
    } else {
      // Encoder is rotating clockwise
      counter++;
    }
  }
  Serial.println(counter);
  previousStateCLK = currentStateCLK;

  if (r == 255 && g < 255 && b == 0) {
    g += 5;
  } else if (r > 0 && g == 255 && b == 0) {
    r -= 5;
  } else if (r == 0 && g == 255 && b < 255) {
    b += 5;
  } else if (r == 0 && g > 0 && b == 255) {
    g -= 5;
  } else if (r < 255 && g == 0 && b == 255) {
    r += 5;
  } else if (r == 255 && g == 0 && b > 0) {
    b -= 5;
  }
}