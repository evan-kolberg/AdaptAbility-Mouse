const int vrx = A0;
const int vry = A1;
const int joystick_click = 8;
const int button1 = 12;
const int button2 = 11;
const int button3 = 10;
const int button4 = 9;

void setup() {
  Serial.begin(9600);
  pinMode(joystick_click, INPUT_PULLUP);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(button4, INPUT);
}

void loop() {
    Serial.print(analogRead(vrx));
    Serial.print(' ');
    Serial.print(analogRead(vry));
    Serial.print(' ');
    Serial.print(digitalRead(joystick_click));
    Serial.print(' ');
    Serial.print(digitalRead(button1));
    Serial.print(' ');
    Serial.print(digitalRead(button2));
    Serial.print(' ');
    Serial.print(digitalRead(button3));
    Serial.print(' ');
    Serial.println(digitalRead(button4));
    delay(120);
}