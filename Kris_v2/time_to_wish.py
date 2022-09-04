import datetime


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak = "Доброе утро!"
    elif hour >= 12 and hour < 18:
        speak = "Добрый день!"
    else:
        speak = "Добрый вечер!"
    return speak
