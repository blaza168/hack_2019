void setup() {
pinMode(9, OUTPUT);
pinMode(10, OUTPUT);
pinMode(11, OUTPUT);
analogWrite(9,10);
analogWrite(10,10);
analogWrite(11,10);

}

void loop() {
analogWrite(9,255);
analogWrite(11,25);
delay(25);
analogWrite(9,25);
analogWrite(10,255);
delay(25);
analogWrite(10,25);
analogWrite(11,255);
delay(25);
analogWrite(9,25);
analogWrite(10,25);
analogWrite(11,25);
delay(200);

}
