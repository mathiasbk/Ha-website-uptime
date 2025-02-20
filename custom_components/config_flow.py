from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN, FETCHURL

import logging

_LOGGER = logging.getLogger(__name__)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Hauptime", data=user_input)

        return self._show_form()

    @callback
    def _show_form(self, errors=None):
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(FETCHURL): str,
            }),
            errors=errors or {},
        )