#include <Arduino.h>
#include <Wire.h>
#include <RH_ASK.h>
#include <SPI.h> // Not actualy used but needed to compile

RH_ASK driver(2000, 12, 11); // 200bps, TX on D11, RX on D12

void setup()
{
  driver.init();
  Serial.begin(9600);  
  Serial.println("Arduino Sensor");

  if (!driver.init())
    Serial.println("Receiver initialization failed");
  else
    Serial.println("Receiver is working");
}

void loop()
{
  float data [4] =  {};
  uint8_t buf[16];
  uint8_t buflen = sizeof(buf);

  if (driver.available () && Serial.available() > 0) // Non-blocking
  {
    char command = Serial.read();
    while (Serial.available() > 0) {
      Serial.read();
    }
    driver.recv(buf, &buflen);
    memcpy(data, (float*)&buf, buflen);

    //    Serial.println(command);

    switch (command) {
      case 'W':
        Serial.print("Light Intensity West (W m-2): ");
        Serial.println(data[0]);
        break;

      case 'E':
        Serial.print("Light Intensity East (W m-2): ");
        Serial.println(data[1]);
        break;

      case 'T':
        Serial.print("Temperature (ºC): ");
        Serial.println(data[2]);
        break;

      case 'H':
        Serial.print("Humidity (%): ");
        Serial.println(data[3]);
        break;

      default:
        break;
    }
  }
  delay(10);
}
