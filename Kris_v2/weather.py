from pyowm import OWM
from pyowm.utils.config import get_default_config
from num2t4ru import num2text


def weather():
    # интеграция с API из openweathermap
    owm = OWM('f571499b1de8ee017956351375a45822')
    mgr = owm.weather_manager()

    # перевод ответа сервера на русский язык
    config_dict = get_default_config()
    config_dict['language'] = 'ru'

    place = 'Минск'

    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    status = w.detailed_status

    if temp > 20:
        recommend = f'На улице очень тепло, ни в чем себе не отказывай :)'
    elif temp < 0:
        recommend = f'На улице холодно пипец как холодно, одевайся как капуста и не забудь шапку!'
    else:
        recommend = f'На улице прохладно, одевайся тепло.'

    temp = round(temp)
    answer = f'В городе {place} сейчас {status}. \nТемпература воздуха составляет {num2text(temp)} градусов цельсия.\n'
    return answer + recommend
