#include "config.h"
#include <WiFi.h>
#include <Wire.h>
#include "HT_SSD1306Wire.h"
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

// WiFi creds
const char* ssid = "helloworld";
const char* password = "aspirin420";

// Server IP and PORT
const char* serverIP = "192.168.2.2";
const int serverPort = 8080;

// Create an instance of the BME280 sensor
Adafruit_BME280 bme;

// Display using default I2C bus
SSD1306Wire display(0x3c, 500000, SDA_OLED, SCL_OLED, GEOMETRY_128_64, RST_OLED); 

// Create a separate I2C bus for the sensor (if supported by your board)
TwoWire I2C_BME280 = TwoWire(1);

WiFiClient client;

void connectToWiFi() {
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void readBME280() {
  float temperature = bme.readTemperature();
  float humidity = bme.readHumidity();
  float pressure = bme.readPressure() / 100.0F;

  Serial.print('\n');
  Serial.print("Temperature: "); Serial.print(temperature); Serial.println(" °C");
  Serial.print("Humidity: "); Serial.print(humidity); Serial.println(" %");
  Serial.print("Pressure: "); Serial.print(pressure); Serial.println(" hPa");

  String data = "Temperature: " + String(temperature) + " °C" + "\n";
  data += "Humidity: " + String(humidity) + " %" + "\n";
  data += "Pressure: " + String(pressure) + " hPa" + "\n";

  String dataToSend = String(temperature) + "," + String(humidity) + "," + String(pressure); 

  // added
  if (client.connect(serverIP, serverPort)) {
    client.print(dataToSend);
    client.stop();
  }

  display.setFont(ArialMT_Plain_10);
  display.setTextAlignment(TEXT_ALIGN_LEFT);

  display.drawString(0, 0, data);
}

void drawText() {
  display.setFont(ArialMT_Plain_10);
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.drawStringMaxWidth(0, 0, 128,
    "Lorem ipsum\n dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore." );
}


void setup() {
  Serial.begin(115200);
  Serial.println("Starting setup...");

  // Connect to WiFi
  connectToWiFi();
  
  // commenting this out fixed the display not working issue!!
  //Wire.begin(); // Initialize default I2C for the display

  display.init();

  if (!display.init()) {
    Serial.println("Display initialization failed!");
    while (1); // Stop if display initialization fails
  }
  
  display.setFont(ArialMT_Plain_10);

  // Initialize second I2C bus for BME280 sensor
  I2C_BME280.begin(4, 5); // SDA on GPIO4, SCL on GPIO5

  if (!bme.begin(0x76, &I2C_BME280)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void loop() {
  // Clear the display
  display.clear();

  // Read BME280 sensor data and display it
  readBME280();

  // drawText();

  // Write the buffer to the display
  display.display();

  // when logging data to screen, use 2000 delay (2 seconds)
  //delay(2000)

  // when sending data to server, use 60000 delay (60 seconds)
  delay(60000);
}
