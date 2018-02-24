#include <Wire.h>
#include <Adafruit_MMA8451.h>
#include <Adafruit_Sensor.h>

// Pins
const int LEFT_CLICK_BTN = 2;
const int RIGHT_CLICK_BTN = 3;
const int ENABLE_MOUSE_BTN = 4;

const int DT = 200; // 500 ms

// State variables

float accel_x_base = 0;
float accel_y_base = 0;
float accel_z_base = 0;

float last_accel_x = 0;
float last_accel_y = 0;
float last_accel_z = 0;

float da_x = 0;
float da_y = 0;
float da_z = 0;

bool left_click = false;
bool right_click = false;
bool mouse_enabled = false;

Adafruit_MMA8451 mma = Adafruit_MMA8451();

void setup(void) {
  // Set up Pins
  
  pinMode(LEFT_CLICK_BTN, INPUT_PULLUP);
  pinMode(RIGHT_CLICK_BTN, INPUT_PULLUP);
  pinMode(ENABLE_MOUSE_BTN, INPUT_PULLUP);


  Serial.begin(9600);
  
  // Set up accelerometer
  
  // wait until the accelerometer connects
  while (!mma.begin()) {
    delay(DT);
  }
  mma.setRange(MMA8451_RANGE_2_G);
}

void loop() {
  if (digitalRead(ENABLE_MOUSE_BTN) == LOW) {
    mouse_enabled = !mouse_enabled;
  }
  left_click = digitalRead(LEFT_CLICK_BTN) == HIGH;
  right_click = digitalRead(RIGHT_CLICK_BTN) == HIGH;
  
  // Read the 'raw' data in 14-bit counts
  mma.read();

  // Get a new sensor event
  sensors_event_t event; 
  mma.getEvent(&event);

  // Regular mouse speed is approx 0.13 m/s for 0.08 m/s hand movement
  
  da_x = event.acceleration.x - last_accel_x;
  da_y = event.acceleration.y - last_accel_y;
  da_z = event.acceleration.z - last_accel_z;
  
  last_accel_x = event.acceleration.x;
  last_accel_y = event.acceleration.y;
  last_accel_z = event.acceleration.z;

  sendSerialData(left_click, right_click, mouse_enabled, da_x, da_y);

  delay(DT);
}

void sendSerialData(const bool left_click,
                    const bool right_click,
                    const bool enabled,
                    const float delta_accel_x,
                    const float delta_accel_y) {
  Serial.print(left_click);      Serial.print(",");
  Serial.print(right_click);     Serial.print(",");
  Serial.print(enabled);         Serial.print(",");
  Serial.print(delta_accel_x);   Serial.print(",");
  Serial.println(delta_accel_y);
}

