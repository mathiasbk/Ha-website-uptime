"""
The skeleton component.

For more details about this component, please refer to the documentation at
"""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.

    # Register the binary_sensor
    hass.helpers.discovery.load_platform('binary_sensor', DOMAIN, {}, config)

    # Register the sensor
    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up hauptime from a config entry."""
    # Set up the component using the configuration entry
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "binary_sensor")
    )

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # Unload the component
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    return await hass.config_entries.async_forward_entry_unload(entry, "binary_sensor")
