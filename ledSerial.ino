const int pinLED = A0;

void setup() {
  Serial.begin(9600);
  pinMode(pinLED, OUTPUT);
}

void loop() {
   if(Serial.available()>0){
      char dato = Serial.read(); 
      
      if(dato == '0'){
        digitalWrite(pinLED,0);
        Serial.println("LED: OFF");
      }
      
      if(dato == '1'){
        digitalWrite(pinLED,1);
        Serial.println("LED: ON");
        }
        
    }
  Serial.println("Arduino te dice Hola");
  delay(1000);
 
}
