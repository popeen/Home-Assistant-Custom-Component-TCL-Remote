import socket
import time

DOMAIN = "tcl_tv_remote"

ATTR_NAME = "key"
ATTR_IP = "ip"
ATTR_PORT = "port"
ATTR_SOURCE = "source"

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""
    
    def keypress(key, ip, port):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        clientSocket.connect((ip,port));
        data = '<?xml version="1.0" encoding="utf-8"?><root><action name="setKey" eventAction="' + key + '" keyCode="' + key + '" /></root>';
        clientSocket.send(data.encode());
    
    def send_key(call):
        """Handle the service call."""
        name = call.data.get(ATTR_NAME)
        ip = call.data.get(ATTR_IP)
        port = call.data.get(ATTR_PORT)
        keypress(name, ip, port);
    
    def go_to_source(call):
        """Handle the service call."""
        source = call.data.get(ATTR_SOURCE)
        ip = call.data.get(ATTR_IP)
        port = call.data.get(ATTR_PORT)
        keypress("TR_KEY_EXIT", ip, port);
        time.sleep(1)
        keypress("TR_KEY_MUTE", ip, port);
        time.sleep(1)
        keypress("TR_KEY_TV", ip, port);
        time.sleep(6)
        keypress("TR_KEY_SOURCE", ip, port);
        time.sleep(1)
        i = 0
        while i < int(source):
            keypress("TR_KEY_DOWN", ip, port);
            i += 1
        keypress("TR_KEY_OK", ip, port);
        time.sleep(1)
        keypress("TR_KEY_MUTE", ip, port);
        
    hass.services.register(DOMAIN, "send_key", send_key)
    hass.services.register(DOMAIN, "go_to_source", go_to_source)
    return True