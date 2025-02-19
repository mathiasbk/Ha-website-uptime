"""
The skeleton component.

For more details about this component, please refer to the documentation at
"""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "hauptime"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.

    #register the binary_sensor
    hass.helpers.discovery.load_platform('binary_sensor', DOMAIN, {}, config)

    return True
