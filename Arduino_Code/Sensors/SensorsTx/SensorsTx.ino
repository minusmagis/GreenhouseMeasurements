#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"
#include <BH1750.h>
#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile

RH_ASK driver(2000, 12, 11); // 200bps, TX on D11, RX on D12

BH1750 lightMeter1;
BH1750 lightMeter2;

bool enableHeater = false;
int loopCnt = 0;

Adafruit_SHT31 sht30 = Adafruit_SHT31();

void setup() {
  Serial.begin(9600);
  Wire.begin();
  driver.init();

  lightMeter1.begin(BH1750::CONTINUOUS_HIGH_RES_MODE, 0x23, &Wire);
  lightMeter2.begin(BH1750::CONTINUOUS_HIGH_RES_MODE, 0x5C, &Wire);
  sht30.begin(0x44); // Set to 0x45 for alternate i2c addr

}

void loop() {
  float data [4] = {float(lightMeter1.readLightLevel() / 44),
                    float(lightMeter2.readLightLevel() / 44),
                    float(sht30.readTemperature()),
                    float(sht30.readHumidity())
                   };

  driver.send((uint8_t *)data, sizeof(data));
  driver.waitPacketSent();
  delay(1000);
}
