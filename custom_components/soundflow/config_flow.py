import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN, CONF_PROVIDER, CONF_NAME, CONF_TOKEN, CONF_COLUMNS, PROVIDERS

class SoundFlowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            provider = user_input[CONF_PROVIDER]
            if provider == "apple_music" and not user_input.get(CONF_TOKEN):
                errors["base"] = "token_required"
            else:
                return self.async_create_entry(title=f"{provider} • {user_input[CONF_NAME]}", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_PROVIDER): vol.In(PROVIDERS),
            vol.Required(CONF_NAME): str,
            vol.Optional(CONF_TOKEN): str,
            vol.Optional(CONF_COLUMNS, default=["playlists", "albums", "artists", "tracks"]): [str]
        })
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return SoundFlowOptionsFlow(config_entry)

class SoundFlowOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema({
            vol.Optional(CONF_COLUMNS, default=self.config_entry.data.get(CONF_COLUMNS, [])): [str]
        })
        return self.async_show_form(step_id="init", data_schema=schema)
