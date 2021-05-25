import os, configparser, requests, json, telebot, nekos
from colorama import Fore, init
init()

config = configparser.ConfigParser()
config.read('config.ini')

Token = config.get("TG-RAIDER", "Token")



if os.name == "nt":
        _ = os.system("cls")

else:
        _ = system("clear")

print(f"""{Fore.RED}

  ____ _    _   _ _____ _____ _   _ 
 / ___| |  | | | |_   _| ____| \ | |
| |  _| |  | | | | | | |  _| |  \| |
| |_| | |__| |_| | | | | |___| |\  |
 \____|_____\___/  |_| |_____|_| \_|

{Fore.RED} Здрасьте, это ГЛЮТЕН и
{Fore.RED} Полное адище начинается ;)""")

bot = telebot.TeleBot(Token)
lol = 'lol'
@bot.message_handler(commands=['spam'])
def auto(message):
    global lol 
    lol = 'lol'
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спам начат")
    while lol == 'lol':
        hentai = nekos.img('random_hentai_gif')
        bot.send_message(message.chat.id, hentai)


@bot.message_handler(commands=['stop'])
def auto(message):
        global lol
        lol = 'nolol'
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спам остановлен")
        bot.send_message(message.chat.id, 'Хентай оверлоад остановлен')


bot.polling(none_stop=True)