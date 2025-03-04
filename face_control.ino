void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);  // Use built-in LED
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');
    message.trim();

    if (message == "ON") {
      digitalWrite(13, HIGH);
      Serial.println("LED ON");
    } else if (message == "OFF") {
      digitalWrite(13, LOW);
      Serial.println("LED OFF");
    }
  }
}

