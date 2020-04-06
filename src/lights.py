from phue import Bridge
import requests
from color_converter_helper import Converter


class lights:
    def __init__(self):
        ip = self.discover_ip()
        self.bridge = Bridge(ip)

    def discover_ip(self):
        response = requests.get('https://discovery.meethue.com')
        if response and response.status_code == 200:
            data = response.json()

            if 'internalipaddress' in data[0]:
                return data[0]['internalipaddress']
            return None

    def lights_connect(self):  
        self.bridge.connect()
        self.bridge.set_group(1, 'on', True)

    def set_light_color(self, color):
        converter = Converter()
        xy = converter.rgb_to_xy(color[0],color[1],color[2])
        self.bridge.set_group(1, 'xy', color)


    def disconnect_lights(self):
        self.bridge.set_group(1, 'on', False)