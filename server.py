import paho.mqtt.client as mqtt
import traceback
from services.resolvers.resolver_selector import ResolverSelector
from services.vehicle.screen import Screen
from services.util.config import Config
from services.publishers.generic_publisher import GenericPublisher
from services.publishers.ping_publisher import PingPublisher
from services.vehicle.keep_alive import KeepAlive
from services.vehicle.lto.overcharge_processor import OverchargeProcessor
from services.vehicle.amplifier.clipping_processor import ClippingProcessor

config = Config()
screen = Screen(config)
keep_alive = KeepAlive(screen)
overcharge_processor = OverchargeProcessor()
clipping_processor = ClippingProcessor()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    try:
        publisher = GenericPublisher(client)
        screen.initialize(publisher)
        client.subscribe(ResolverSelector.VOLTAGES_TOPIC)
        client.subscribe(ResolverSelector.KEEP_ALIVE_TOPIC)
        client.subscribe(ResolverSelector.CLIPPING_TOPIC)
        PingPublisher(client, keep_alive).run()
    except Exception as ex:
        traceback.print_exc()


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        selector = ResolverSelector(msg.topic)
        resolver = selector.resolver()
        resources = {
            "config": config,
            "screen": screen,
            "keep_alive": keep_alive,
            "overcharge_processor": overcharge_processor,
            "clipping_processor": clipping_processor
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
