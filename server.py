import paho.mqtt.client as mqtt
import traceback
from services.resolvers.resolver_selector import ResolverSelector
from services.vehicle.screen import Screen
from services.util.config import Config
from services.publishers.ping_publisher import PingPublisher
from services.vehicle.keep_alive import KeepAlive

config = Config()
screen = Screen(config)
keep_alive = KeepAlive(screen)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    try:
        screen.initialize()
        client.subscribe("vehicle/lto/voltages")
        client.subscribe(PingPublisher.KEEP_ALIVE_TOPIC)
        PingPublisher(client, keep_alive).run()
    except Exception as ex:
        traceback.print_exc()


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        selector = ResolverSelector(msg.topic)
        resolver = selector.resolver()
        resources = {
            "screen": screen,
            "keep_alive": keep_alive
        }

        resolver.resolve(msg.payload, resources)
    except Exception as ex:
        traceback.print_exc()


def on_disconnect(client, userdata, rc):
    screen.close()
    print(f"Disconnected with result code {str(rc)}")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.on_disconnect = on_disconnect

mqtt_client.connect(config.mqtt_host, config.mqtt_port)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqtt_client.loop_forever()
