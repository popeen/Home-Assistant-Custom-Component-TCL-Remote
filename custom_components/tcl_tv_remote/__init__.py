from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from tcltvremote import TclTvRemote

import socket
import time

DOMAIN = "tcl_tv_remote"

ATTR_KEY = "key"
ATTR_IP = "ip"
ATTR_PORT = "port"
ATTR_SOURCE = "source"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return True

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""
    
    def send_key(call):
        """Handle the service call."""
        tv = TclTvRemote(call.data.get(ATTR_IP), int(call.data.get(ATTR_PORT)))
        tv.keypress(call.data.get(ATTR_KEY));
    
    def go_to_source(call):
        """Handle the service call."""
        tv = TclTvRemote(call.data.get(ATTR_IP), int(call.data.get(ATTR_PORT)))
        tv.go_to_source(call.data.get(ATTR_SOURCE))
        
    hass.services.register(DOMAIN, "send_key", send_key)
    hass.services.register(DOMAIN, "go_to_source", go_to_source)
    return True