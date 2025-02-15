from homeassistant import core
from homeassistant.core import ServiceCall


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the ha-website-uptime component."""
    async def handle_force_check(call: ServiceCall):
        hass.states.set("hello world", "test")
    return True