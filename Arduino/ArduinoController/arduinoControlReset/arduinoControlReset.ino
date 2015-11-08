
/*
MOSI: Pin 51
* MISO: Pin 50
* SCK: Pin 52
* SDA: Pin 10
* RST: Pin 9
*/

#include <SPI.h>
#include <RFID.h>


#define SS_PIN 10
#define RST_PIN 9

int serNum0;
int serNum1;
int serNum2;
int serNum3;
int serNum4;




long previousMillis = 0;

long interval = 3000;
int counter = 0;


RFID rfid(SS_PIN, RST_PIN);


void setup() {

  Serial.begin(9600);
  SPI.begin();
  rfid.init();

}

void loop() {

  unsigned long currentMillis = millis();

  
    
 
  if (rfid.isCard()) {
    if (rfid.readCardSerial()) {
      // checks if id is the same, if not, print out new card data
      if ((rfid.serNum[0] != serNum0
           && rfid.serNum[1] != serNum1
           && rfid.serNum[2] != serNum2
           && rfid.serNum[3] != serNum3
           && rfid.serNum[4] != serNum4
          ) || (currentMillis - previousMillis >= interval)) {
        //reset the time for next tag
        previousMillis = currentMillis;
        serNum0 = rfid.serNum[0];
        serNum1 = rfid.serNum[1];
        serNum2 = rfid.serNum[2];
        serNum3 = rfid.serNum[3];
        serNum4 = rfid.serNum[4];

        //prints the RFID Tag number to the serial
        Serial.println("RFID");
        Serial.println(rfid.serNum[0], DEC);
        Serial.println(rfid.serNum[1], DEC);
        Serial.println(rfid.serNum[2], DEC);
        Serial.println(rfid.serNum[3], DEC);
        Serial.println(rfid.serNum[4], DEC);
        
      }
    }
  }
  rfid.halt();
  

  
}




