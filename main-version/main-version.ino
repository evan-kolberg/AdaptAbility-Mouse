const int vrx = A0;
const int vry = A1;
const int sw = 8;
const int button1 = 12;
const int button2 = 11;

void setup() {
  Serial.begin(9600);
  pinMode(sw, INPUT_PULLUP);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
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
    Serial.println(digitalRead(button2));
}