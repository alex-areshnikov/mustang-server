from unittest.mock import patch
from services.publishers.generic_publisher import GenericPublisher


class TestGenericPublisher(object):
    @patch.object(GenericPublisher, 'publish')
    def test_it_publishes_charging(self, mock_publish):
        publisher = GenericPublisher(None)
        publisher.charging("Payload")
        mock_publish.assert_called_once_with("vehicle/lto/charge", "Payload")

    @patch.object(GenericPublisher, 'publish')
    def test_it_publishes_charging(self, mock_publish):
        publisher = GenericPublisher(None)
        publisher.trunk_lights("Payload")
        mock_publish.assert_called_once_with("vehicle/trunk/lights", "Payload")
