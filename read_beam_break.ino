// reads a potentiometer and sends value over serial --> modified so that beam sensor functions as potentiometer
// set up arduino: https://learn.adafruit.com/ir-breakbeam-sensors/arduino
// communicating with python: https://pythonforundergradengineers.com/python-arduino-potentiometer.html

// this sketch causes LED to turn off when the beam is broken
// play around with different sensorValue thresholds to decide what number to use to designate a beam break
// after uploading sketch and closing Arduino IDE, run read_arduino.py to get beam break output in python

int sensorPin = A0;  // The potentiometer on pin 0                  
int ledPin = 13;     // The LED is connected on pin 13
int sensorValue;     // variable to stores data

void setup() // runs once when the sketch starts
{
  // make the LED pin (pin 13) an output pin
  pinMode(ledPin, OUTPUT);
  
  // initialize serial communication
  Serial.begin(9600);
}

void loop() // runs repeatedly after setup() finishes
{
  sensorValue = analogRead(sensorPin);  // read pin A0   
  Serial.println(sensorValue);         // send data to serial

  if (sensorValue == 0) {             
    digitalWrite(ledPin, HIGH); }     // Turn the LED off

  else {                               
    digitalWrite(ledPin, LOW); }     // Keep the LED on

  delay(100);             // Pause 100 milliseconds
}
