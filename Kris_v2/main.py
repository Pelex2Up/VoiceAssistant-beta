# Крис v2.0

import datetime
import random
import webbrowser

from fuzzywuzzy import fuzz

import config
import stt
import tts
from weather import *
import time_to_wish

print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")

tts.va_speak(f'{time_to_wish.wish_me()}. Меня зовут Крис. Я ваш голосовой ассистент. Спросите меня что я умею делать.')


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаемся к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "сообщать погоду ..."
        text += "и открывать браузер"
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # время сейчас
        now = datetime.datetime.now()
        text = "Сейчас " + num2text(now.hour) + " " + num2text(now.minute)
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... эксе эксе эксе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «можно присоединиться?»',
                 'Интересный факт: девяносто процентов причин поломки компьютера — сидят напротив него.',
                 """Звонок в службу технической поддержки:
                    — У меня компьютер не видит принтер; я уже и монитор на него повернула, а он всё равно пишет, 
                    что его не видит. Что делать?.. — А вы пальцем показывали?""",
                 """Джун должен знать все алгоритмы.
                    Мидл должен знать о существовании всех алгоритмов.
                    Сеньор должен знать, где сидит джун."""]
        tts.va_speak(random.choice(jokes))

    elif cmd == 'hello':
        hello_sir = 'Приветствую, мой создатель. Чем я могу тебе помочь?'
        tts.va_speak(hello_sir)

    elif cmd == 'weather_minsk':
        tts.va_speak(weather())

    elif cmd == 'open_browser':
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("http://python.org")


# начать прослушивание команд
stt.va_listen(va_respond)
