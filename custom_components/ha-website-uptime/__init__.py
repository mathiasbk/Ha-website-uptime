from homeassistant import core
from homeassistant.core import ServiceCall
from .binary_sensor import check_website_status


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the ha-website-uptime component."""
    async def handle_force_check(call: ServiceCall):
        url = call.data.get("url")
        result = await check_website_status(url)
        hass.bus.async_fire(f"{DOMAIN}_forced_check", {"url": url, "result": result})

    hass.services.async_register(DOMAIN, "force_check", handle_force_check)
    return True