import paho.mqtt.client as mqtt
import requests
import json

# Konfigurasi MQTT
broker_address = "localhost"
topic = "airQuality/data"
result_topic = "airQuality/result"

# Callback saat terima pesan
def on_message(client, userdata, message):
    try:
        print(f"Message received: {message.payload.decode('utf-8')}")
        sensor_data = json.loads(message.payload.decode("utf-8"))
        
        # Kirim data ke API Fyang digunakan untuk prediksi
        response = requests.post('http://localhost:5000/api/predict', json=sensor_data)
        
        if response.status_code == 200:
            result = response.json()
            # mendapatkan hasil prediksi
            asthma_attack = result.get('asthma_attack')
            if asthma_attack is not None:
                print(f"Prediction result: {asthma_attack}")
                client.publish(result_topic, str(asthma_attack))
            else:
                print(f"Prediction result not found in the response: {result}")
        else:
            print(f"Failed to send data to API, status code: {response.status_code}, response: {response.text}")
    except Exception as e:
        print(f"Error processing message: {e}")

# Callback terhubung ke mosquitto
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

# Konfigurasi client MQTT
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

try:
    print("Connecting to MQTT broker...")
    client.connect(broker_address)
    print("Connected to MQTT broker")
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")

print(f"Subscribing to topic '{topic}'")
client.loop_forever()
