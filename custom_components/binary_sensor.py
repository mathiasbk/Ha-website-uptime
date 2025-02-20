import logging
import requests
import voluptuous as vol

from homeassistant import core, config_entries
from homeassistant.components.binary_sensor import BinarySensorEntity, PLATFORM_SCHEMA
from homeassistant.const import CONF_HOST

from .const import DOMAIN, FETCHURL

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): str,
})

async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([SiteUpSensor(config[FETCHURL])])

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([SiteUpSensor(config_entry.data[FETCHURL])])


class SiteUpSensor(BinarySensorEntity):
    _attr_name = "Site Up"
    _attr_device_class = "connectivity"

    def __init__(self, url):
        self._state = False
        self._url = url
    
    @property
    def name(self):
        return self._attr_name
 
    @property
    def is_on(self):
        return self._state

    def update(self):
        try:
            response = requests.get(self._url)
            _LOGGER.info("Fetching URL: %s", self._url)

            if response.status_code == 200:
                self._state = True
            else:
                self._state = False
        except:
            self._state = False
            _LOGGER.error("Failed to fetch URL: %s", self._url)