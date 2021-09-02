
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



owm = OWM('51e76a3a0a455d3e3e0620661d175c0e')
mgr = owm.weather_manager()

def get_clouds(city):
# Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(city)
    w = observation.weather
    return w.clouds
