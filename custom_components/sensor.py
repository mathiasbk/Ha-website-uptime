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

async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([URLSensor(config[FETCHURL])])

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([URLSensor(config_entry.data[FETCHURL])], ResponseTimeSensor(config_entry.data[FETCHURL]))


class URLSensor(SensorEntity):
    _attr_name = "Site URL"

    def __init__(self, url):
        self._state = url
        self._url = url
        #self.hass.bus.async_listen("update_responsetime", self.update)
    
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
    
    @property
    def name(self):
        return self._attr_name
    
    @property
    def state(self):
        return self._state
    
    def update(self):
        return self._state