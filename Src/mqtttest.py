import paho.mqtt.client as mqtt
import time

broker="ec2-54-74-124-135.eu-west-1.compute.amazonaws.com"

def on_connect(client, userdata, flags, rc):
    print("Connected")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, 1883, 60)
for i in range(3):
    
    print("send {i} to a/b")
    time.sleep(1)
client.publish('test', payload=90, qos=0, retain=False)
client.loop_forever()

 



 

 

