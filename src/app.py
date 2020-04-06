# get an image from unsplash
# get the major color from unsplash
# convert that color into whatever format hues needs
# set lamps to that color

from time import sleep
from lights import lights

lights = lights()


def run_app(sleep_time):
    while True:

        # run the entire app here         

        sleep(sleep_time)

def kill_app():
    lights.disconnect_lights()