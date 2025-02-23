import logging
import requests
import voluptuous as vol

from homeassistant import core, config_entries
from homeassistant.components.binary_sensor import BinarySensorEntity, PLATFORM_SCHEMA
from homeassistant.const import CONF_HOST
from homeassistant.helpers.dispatcher import async_dispatcher_send

from .const import DOMAIN, FETCHURL

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(FETCHURL, default="http://google.com"): str,
})

async def async_setup_platform(hass, config_entry, async_add_entities, discovery_info=None):
    _LOGGER.debug("Setting up SiteUpSensor with URL: %s", config_entry.data[FETCHURL])
    async_add_entities([SiteUpSensor(hass, config_entry.data[FETCHURL])])

async def async_setup_entry(hass, config_entry, async_add_entities):
    _LOGGER.debug("Setting up SiteUpSensor with URL: %s", config_entry.data[FETCHURL])
    async_add_entities([SiteUpSensor(hass, config_entry.data[FETCHURL])])
    

class SiteUpSensor(BinarySensorEntity):
    _attr_name = "Site Up"
    _attr_device_class = "connectivity"

    def __init__(self, hass, url):
        self.hass = hass
        self._state = False
        self._url = url
    
    @property
    def name(self):
        return self._attr_name
 
    @property
    def is_on(self):
        return self._state

    async def async_update(self):
        try:
            response = await self.hass.async_add_executor_job(requests.get, self._url)
            _LOGGER.info("Fetching URL: %s", self._url)
            _LOGGER.info("Responsetime in seconds: %s", response.elapsed.total_seconds())

            # Send responsetime to the responsetime sensor
            self.hass.async_add_job(
                async_dispatcher_send, self.hass, "update_responsetime", response.elapsed.total_seconds()
            )

            if response.status_code == 200:
                self._state = True
            else:
                self._state = False

        except Exception as e:
            self._state = False
            _LOGGER.error("Failed to fetch URL: %s, Error: %s", self._url, str(e))