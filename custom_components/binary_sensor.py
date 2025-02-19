import logging
import requests
from homeassistant.components.binary_sensor import BinarySensorEntity

_LOGGER = logging.getLogger(__name__)

DOMAIN = "hauptime"
FetchURL = "https://www.google.com"

def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([SiteUpSensor()])

class SiteUpSensor(BinarySensorEntity):
    _attr_name = "Site Up"
    _attr_device_class = "connectivity"

    def __init__(self):
        self._state = False
    
    @property
    def name(self):
        return self._attr_name
 
    @property
    def is_on(self):
        return self._state

    def update(self):
        try:
            response = requests.get(FetchURL)
            if response.status_code == 200:
                self._state = True
            else:
                self._state = False
            self._state = True
        except:
            self._state = False
            _LOGGER.error("Failed to fetch URL: %s", FetchURL)