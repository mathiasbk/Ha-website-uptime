from homeassistant.helpers.entity import BinarySensorEntity
from .const import DOMAIN, CONF_URL, CONF_NAME, DEFAULT_SCAN_INTERVAL

async def async_setup_entry(hass, config_entry, async_add_entities):
    url = config_entry.data[CONF_URL]
    name = config_entry.data[CONF_NAME]