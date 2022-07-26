from randomity import Randomity
from Config.config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)
_r = Randomity


# start
@bot.message_handler(commands=['start'])
def cat(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!\n\n'
                                      f"It's high quality managment of random pictures. "
                                      f"The Randomity can entertain your group's members with funny photos on different topics which are shown below. \n\n"
                                      f'• cats pictures (command: /cat)\n'
                                      f'• dogs pictures (command: /dog)\n'
                                      f'• ducks pictures (command: /duck)\n'
                                      f'• foxes pictures (command: /fox)\n'
                                      f'• neko-tyans pictures (command: /neko)</i>\n\n'
                                      f"You can add the bot to your group or use it in your PM. "
                                      f"<b>The Randomity doesn't need any admin rights in a group!</b>\n\n"
                                      f'Thanks for using my service :)', parse_mode='html')


# random animals
@bot.message_handler(commands=['cat'])
def cat(message):
    bot.send_photo(message.chat.id, _r(message).get_random('https://aws.random.cat/meow', 'file'),
                   caption=f"A random picture just for you, {str(message.from_user.first_name).title()}!")


@bot.message_handler(commands=['dog'])
def dog(message):
    bot.send_photo(message.chat.id, _r(message).get_random('https://dog.ceo/api/breeds/image/random', 'message'),
                   caption=f"A random picture just for you, {str(message.from_user.first_name).title()}!")


@bot.message_handler(commands=['duck'])
def duck(message):
    bot.send_photo(message.chat.id, _r(message).get_random('https://random-d.uk/api/random', 'url'),
                   caption=f"A random picture just for you, {str(message.from_user.first_name).title()}!")


@bot.message_handler(commands=['fox'])
def fox(message):
    bot.send_photo(message.chat.id, _r(message).get_random('https://randomfox.ca/floof/', 'image'),
                   caption=f"A random picture just for you, {str(message.from_user.first_name).title()}!")


# random tyan
@bot.message_handler(commands=['neko'])
def neko(message):
    bot.send_photo(message.chat.id, _r(message).get_random('http://api.nekos.fun:8080/api/neko', 'image'),
                   caption=f"A random picture just for you, {str(message.from_user.first_name).title()}!")


bot.polling(none_stop=True)