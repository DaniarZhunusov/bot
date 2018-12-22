import random

import requests
import vk_api
from config import *


def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000)})


vk_bot = vk_api.VkApi(token=TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print("готов к работе")
# + str(long_poll))

while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                       act='a_check',
                                                                       key=key,
                                                                       ts=ts)).json()
    update = long_poll['updates']
    if update[0][0] == 4:
        if update[0][6] == 'Привет' :
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            write_msg(user_id, 'Привет, ' + (user_name[0]['first_name']))  # сообщение пользователю
        if update[0][6] == 'Понедельник':
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            write_msg(user_id, '1 Биология (4.3.11) ; 2 Физика (2.3.06) ; 3 Физ-ра ; 4 Английский язык (4.3.03) ; 5 Геометрия (1.3.03) ; 6 Алгебра (1.3.03), ' + (user_name[0]['first_name']))  # сообщение пользователю
        elif update[0][6] == 'Вторник':
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            write_msg(user_id, '1 ОБЖ (1.3.05) ; 2 Лит-ра (4.3.08) ; 3 Русский язык (4.3.08) ; 4 История (4.3.12) ; 5 Алгебра (3.2.06) ; 6 Музыка (4.3.06), ' + (user_name[0]['first_name']))  # сообщение пользователю
        elif update[0][6] == 'Среда':
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            write_msg(user_id,'1 Технология (1.4.01) ; 2 Технология (1.4.01) ; 3 Физ-ра ; 4 География (1.3.05) ; 5 Информатика (3.3.13) ; 6 Русский язык (2.3.02), ' + (user_name[0]['first_name']))  # сообщение пользователю
        elif update[0][6] == 'Четверг':
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            write_msg(user_id,'1 История (4.3.12) ; 2 Физика (2.3.06) ; 3 Английский язык (4.3.03) ; 4 Обществознание (4.3.12) 5 Алгебра (1.3.01) ; 6 ИЗО (4.12.02), ' + (user_name[0]['first_name']))  # сообщение пользователю
        elif update[0][6] == 'Пятница':
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            write_msg(user_id,'1 Русский язык (4.3.08) ; 2 Алгебра (2.3.01) ; 3 Геометрия (2.3.01) ; 4 История (4.3.12) ; 5 Физ-ра, ' + (user_name[0]['first_name']))  # сообщение пользователю
        elif update[0][6] == 'Суббота':
            user_id = update[0][3]
            user_name = vk_bot.method('users.get', {'user_ids': user_id})
            write_msg(user_id,'1 География (1.3.05) ; 2 Английский язык (4.3.03) ; 3 Русский язык (3.2.07) ; 4 Лит-ра (3.2.07) 5 Биология (4.3.11) ; 6 История СПБ (4.3.12), ' + (user_name[0]['first_name']))  # сообщение пользователю
            print(str(user_name[0]['first_name']) + ' ' +
              str(user_name[0]['last_name']) + 'написал(а) боту - ' + str(update[0][6]))  # сообщение нам
    # Меняем ts для следующего запроса
    ts = long_poll['ts']
