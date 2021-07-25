import eel
from pyowm import OWM

eel.init("web")    

owm = OWM('79dcbcbc0cc9b4212b1c30418cf3ba14')
mgr = owm.weather_manager()

@eel.expose
def getTemp(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    t = w.temperature("celsius")
    t1 = t["temp"]

    return str(t1) + " °C"

@eel.expose
def getFeels(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    t = w.temperature("celsius")
    t2 = t["feels_like"]

    return str(t2) + " °C"

@eel.expose
def getWind(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather   
    wi = w.wind()['speed']

    return str(wi) + " М/С" 

@eel.expose
def getHum(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather   

    return str(w.humidity) 

@eel.expose
def getClouds(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather   

    return str(w.clouds)

@eel.expose
def getStatus(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather   

    return str(w.detailed_status) 



eel.start("index.html", size = (800,670))