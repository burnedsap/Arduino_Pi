import processing.serial.*;
import cc.arduino.*;

Arduino arduino;
int ledPin = 10;

void setup()
{
  //println(Arduino.list());
  arduino = new Arduino(this, Arduino.list()[3], 57600);
  arduino.pinMode(ledPin, Arduino.INPUT);
 
}

void draw()
{
  /*arduino.digitalWrite(ledPin, Arduino.HIGH);
  delay(1000);
  arduino.digitalWrite(ledPin, Arduino.LOW);
  delay(1000);
  */
  
  println(arduino.analogRead(ledPin));
  //delay(500);

}