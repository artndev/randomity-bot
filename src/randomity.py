import requests
from main import bot

class Randomity():

    def __init__(self, message):
        self.message = message

    def get_random(self, api, key):
        if self.message.chat.type not in ['group', 'private']:
            return None

        response = requests.get(api)
        source = requests.get(str(response.json()[key]).replace(r'\\', " "))

        with open('Assets/sample.jpg', 'wb') as sample:
            sample.write(source.content)

        sample_after = open('Assets/sample.jpg', 'rb')
        return sample_after

