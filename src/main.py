from randomity import Randomity
from Config.config import bot

# start
@bot.message_handler(commands=['start'])
def cat(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!\n\n'
                                      f"It's high quality managment of random pictures. "
                                      f"The Randomity can entertain your group's members with funny photos on different topics which are shown below. \n\n"
                                      f'• cats pictures <i>(command: /cat)</i>\n'
                                      f'• dogs pictures <i>(command: /dog)</i>\n'
                                      f'• ducks pictures <i>(command: /duck)</i>\n'
                                      f'• foxes pictures <i>(command: /fox)</i>\n'
                                      f'• neko-tyans pictures <i>(command: /neko)</i>\n\n'
                                      f"You can add the bot to your group or use it in your PM. "
                                      f"<b>The Randomity doesn't need any admin rights in a group!</b>\n\n"
                                      f'Thanks for using my service :)', parse_mode='html')


# random animals
@bot.message_handler(commands=['cat'])
def cat(message):
    Randomity(message).get_random('https://aws.random.cat/meow', 'file')


@bot.message_handler(commands=['dog'])
def dog(message):
    Randomity(message).get_random('https://dog.ceo/api/breeds/image/random', 'message')


@bot.message_handler(commands=['duck'])
def duck(message):
    Randomity(message).get_random('https://random-d.uk/api/random', 'url')


@bot.message_handler(commands=['fox'])
def fox(message):
    Randomity(message).get_random('https://randomfox.ca/floof/', 'image')


# random tyan
@bot.message_handler(commands=['neko'])
def neko(message):
    Randomity(message).get_random('http://api.nekos.fun:8080/api/neko', 'image')


bot.polling(none_stop=True)