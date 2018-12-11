 #!/usr/bin/env python

import paho.mqtt.client as mqtt
from resolvers.resolver_selector import ResolverSelector

MQTT_HOST = "mustang.local"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print "Connected with result code "+str(rc)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("vehicle/lto/voltages")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):    
    selector = ResolverSelector(msg.topic)
    resolver = selector.resolver()
    resolver.resolve(msg.payload)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_HOST, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqtt_client.loop_forever()
