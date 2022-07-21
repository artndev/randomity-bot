import requests
from Config.config import bot

class Randomity():

    def __init__(self, message):
        self.message = message


    def get_random(self, api, key, type = 'picture'):
        if self.message.chat.type not in ['group', 'private']:
            return None

        response = requests.get(api)
        source = requests.get(str(response.json()[key]).replace(r'\\', " "))

        with open('Assets/sample.jpg', 'wb') as sample:
            sample.write(source.content)

        sample_after = open('Assets/sample.jpg', 'rb')
        bot.send_photo(self.message.chat.id, sample_after,
                       caption=f"<a href='{source}'>A random {type} just for you, {str(self.message.from_user.first_name).capitalize()}!</a>",
                       parse_mode='html')
