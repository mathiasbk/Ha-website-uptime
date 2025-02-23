import logging
import requests
import voluptuous as vol

from homeassistant import core, config_entries
from homeassistant.components.sensor import SensorEntity, PLATFORM_SCHEMA
from homeassistant.const import CONF_HOST
from homeassistant.helpers.dispatcher import async_dispatcher_connect

from .const import DOMAIN, FETCHURL

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): str,
})

async def async_setup_platform(hass, config_entry, add_entities, discovery_info=None):
    add_entities([URLSensor(config_entry.data[FETCHURL]), ResponseTimeSensor(config_entry.data[FETCHURL])])

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([URLSensor(config_entry.data[FETCHURL]), ResponseTimeSensor(config_entry.data[FETCHURL])])


class URLSensor(SensorEntity):
    _attr_name = "Site URL"

    def __init__(self, url):
        self._state = url
        self._url = url
    
    @property
    def name(self):
        return self._attr_name
 
    @property
    def state(self):
        return self._state

class ResponseTimeSensor(SensorEntity):
    _attr_name = "Response Time"

    def __init__(self, url):
        self._state = None
        self._url = url
        _LOGGER.debug("ResponseTimeSensor initialized with URL: %s", url)
    
    @property
    def name(self):
        return self._attr_name
    
    @property
    def state(self):
        return self._state
    
    def handle_update(self, value):
        self._state = value
        self.hass.async_add_job(self.async_write_ha_state)
        _LOGGER.debug("ResponseTimeSensor updated with value: %s", value)
    
    def async_added_to_hass(self):
        self.async_on_remove(
            async_dispatcher_connect(self.hass, "update_responsetime", self.handle_update)
        )
        _LOGGER.debug("ResponseTimeSensor added to HASS")