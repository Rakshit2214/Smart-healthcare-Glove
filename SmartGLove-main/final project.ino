#include <Wire.h>
#include "MAX30100_PulseOximeter.h"
// Load Wi-Fi library
// #include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <OneWire.h>
#include <DallasTemperature.h>
// GPIO where the DS18B20 is connected to
const int oneWireBus = D4; 
// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);
// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);


#define REPORTING_PERIOD_MS     1000
float BPM, SpO2, temperature;

// Replace with your network credentials
const char* ssid     = "canon32";
const char* password = "raklipi123";

// Create a PulseOximeter object
// Connections : SCL PIN - D1 , SDA PIN - D2 , INT PIN - D0
PulseOximeter pox;
// Time at which the last beat occurred
uint32_t tsLastReport = 0;


// Callback routine is executed when a pulse is detected
void onBeatDetected() {
    // Serial.println("Beat!");
}

void setup() {
    Serial.begin(115200);
    //while(!Serial) { }
    

    Serial.println("Initializing pulse oximeter..");
    // Initialize sensor
    if (!pox.begin()) {
        Serial.println("POX-FAILED");
        for(;;);
    } else {
        Serial.println("SUCCESS");
        
    }

    // Configure sensor to use 7.6mA for LED drive
    pox.setIRLedCurrent(MAX30100_LED_CURR_7_6MA);
    //pox.setIRLedCurrent(MAX30100_LED_CURR_11MA);
    // pox.setIRLedCurrent(MAX30100_LED_CURR_14_2MA);
    // pox.setIRLedCurrent(MAX30100_LED_CURR_17_4MA);
    // pox.setIRLedCurrent(MAX30100_LED_CURR_24MA);


    // Register a callback routine
    pox.setOnBeatDetectedCallback(onBeatDetected);


  
sensors.begin();
}

void loop() {


  pox.update();
    // Grab the updated heart rate and SpO2 levels

    if (millis() - tsLastReport > REPORTING_PERIOD_MS) {
      // Read from the sensor

        BPM = pox.getHeartRate();
        SpO2 = pox.getSpO2();
        Serial.println(BPM);

        Serial.println(SpO2);
    
        

    sensors.setWaitForConversion(false);
    sensors.requestTemperatures(); 
    sensors.setWaitForConversion(true);
  float temperatureF = sensors.getTempFByIndex(0);
  //float temperatureF = sensors.getTempFByIndex(0);
  temperature = temperatureF;
  
  Serial.println(temperatureF);

  //Serial.print(temperatureF);
  //Serial.println("*F");


        tsLastReport = millis();
    }

    
}