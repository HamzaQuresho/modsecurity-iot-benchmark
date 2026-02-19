import paho.mqtt
import paho.mqtt.client as mqtt
import http.client
import json
import time

# MQTT broker details
mqtt_host = "192.168.0.41"
mqtt_port = 1883
mqtt_topic = "sensor/data/#"  # Subscribing to all subtopics under sensor/data

# HTTP server details
http_host = "192.168.0.41"
http_port = 80
http_path = "/handle_MQTTpost.php"  # Path to the PHP script

# Counter 
msg_count = 0

# MQTT callback function
def on_message(client, userdata, msg):
    global msg_count

    msg_count += 1
    payload = msg.payload.decode()  # Decode the byte payload to string
    print(f"Received MQTT message #{msg_count} on topic: {msg.topic} with payload: {payload}")

    try:
        # Create HTTP connection
        http_conn = http.client.HTTPConnection(http_host, http_port)
        
        # Construct JSON data
        data = json.dumps({"topic": msg.topic, "payload": payload})
        
        # Construct HTTP request headers
        headers = {'Content-type': 'application/json'}

        # Send HTTP POST request
        http_conn.request("POST", http_path, body=data, headers=headers)

        response = http_conn.getresponse()
        print(response.status, response.reason)
        print(response.read().decode())  # decode() to convert bytes to str

        http_conn.close()

        print(f"Forwarded MQTT message #{msg_count} to HTTP")
    except Exception as e:
        print(f"Failed to forward MQTT message #{msg_count} to HTTP: {e}")

# Create MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect and subscribe 
print(f"Connecting to MQTT broker at {mqtt_host}:{mqtt_port}")
client.connect(mqtt_host, mqtt_port)

print(f"Subscribing to MQTT topic: {mqtt_topic}")
client.subscribe(mqtt_topic)

# Loop forever
client.loop_forever()
