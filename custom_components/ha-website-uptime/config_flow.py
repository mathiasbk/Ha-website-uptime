from homeassistant import config_entries
from .const import CONF_name
from .const import DOMAIN

class WebsiteMonitorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.async_create_entry(title=user_input[CONF_name], data=user_input)

