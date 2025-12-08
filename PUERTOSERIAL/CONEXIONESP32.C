#include<WiFi.h>
#include<PubSubClient.h>

const char* ssid = "TECSJ";
const char* password = "TECMM2025";
const char* mqttServer = "broker.emqx.io"; //Nombre del broker https://www.emqx.com/en/mqtt/public-mqtt5-broker
int port = 1883; //puerto
String stMac;
char mac[50];
char clientId[50];

WiFiClient espClient;
PubSubClient client(espClient);

#define ledPin 13


void setup() {
Serial.begin(115200);
randomSeed(analogRead(0)); //basico para evitar interferencias  marcar ocupado

delay(10);
Serial.print("\n Conecatando a: ");
Serial.print(ssid);

wifiConnect();

Serial.println("\n Wifi conectado");
Serial.println("Dirección IP");
Serial.println(WiFi.localIP());
Serial.println(WiFi.macAddress());
stMac = WiFi.macAddress();
stMac.replace(":","_");
Serial.println(stMac);

client.setServer(mqttServer, port);// establece coneccion con broker
client.setCallback(callback);// secuecia pendiente de los cambios ocurridos 
pinMode(ledPin, OUTPUT);

}

void wifiConnect(){
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
}

void mqttReconnect(){
  while(!client.connected()){//mientas no se conecta 
    Serial.print("Intentando conectar esta madre de MQTT");
    long r = random(1000);
    sprintf(clientId, "clientId-%ld", r);//se obtiene el id del cliente 
    if (client.connect(clientId)){// si el cliente se conecta 
      Serial.print(clientId);
      Serial.println("Conectando");
      client.subscribe("topicName_led");// el cliente se suscribe a un topico 
      client.publish("topicName_pub", "HolaMundo,ESP32 Conectado!!");
    }else{
      Serial.print("fallo, rc=");
      Serial.print(client.state());// estado del cliente
      Serial.println("siguinete intento en 5 seg...");
      delay(5000);
    }
  }
}

void callback(char* topic, byte* message, unsigned int lenght){
  Serial.print("llego un mensaje en el topico");
  Serial.print(topic);
  Serial.print(". Mensaje: ");
  String setMessage;
  for(int i=0; i<lenght; i++){
    setMessage = setMessage + (char)message[i];
  }

  Serial.println(setMessage);

  if(String(topic)=="topicName_led"){
    if(setMessage == "on"){
      digitalWrite(ledPin, HIGH);
      client.publish("topicName_pub", "Encendido");
    }else if(setMessage == "off"){
      digitalWrite(ledPin, LOW);
      client.publish("topicName_pub", "Apagado");

    }
  }

}
void loop() {
delay(50);
if(!client.connected()){
  mqttReconnect();
}
client.loop();
}
