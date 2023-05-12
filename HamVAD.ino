String inputString = "";
bool stringComplete = false;
int val = 0;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
  pinMode(10,OUTPUT);
  pinMode(LED_BUILTIN ,OUTPUT);
}

void loop() {
  char inChar = (char)Serial.read();
  val = val-1;
  if (inChar == '1')
    val = val+30;
  analogWrite(10,val);
  if (val > 255)
    val = 255;
  if (val < 0)
    val = 0;
  delay(10);
}
