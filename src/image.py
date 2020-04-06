import requests
import shutil
from PIL import Image


class images:
    def __init__(self):
        self.url = 'https://source.unsplash.com/random'

    def get_image(self):
        response = requests.get(url, stream=True)
        with open('img.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

        del response
        return Image.open('img.png')

