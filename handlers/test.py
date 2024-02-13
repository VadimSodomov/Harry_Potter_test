import telebot.types

from telebot.handler_backends import StatesGroup, State

from handlers.funcs import get_question, get_good, get_bad, result, get_answers_current, questions, get_last_chislo_in_str
from init_bot import bot


attributes = {f'Question{i}': State() for i in range(1, len(questions)+1)}

# Создание класса с динамически добавленными состояниями
Questions = type('Questions', (StatesGroup,), attributes)


@bot.callback_query_handler(func=lambda callback: callback.data == "start")
def question1(callback: telebot.types.CallbackQuery):
    bot.set_state(callback.from_user.id, attributes[f"Question{1}"], callback.message.chat.id)
    get_question(callback, 0)
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        data["scores"] = 0


@bot.callback_query_handler(state=attributes[f"Question{len(questions)}"], func=lambda callback: callback.data == "good")
def good_answer_final(callback: telebot.types.CallbackQuery):
    bot.send_message(callback.message.chat.id, "Молодец! Верно)")
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        data["scores"] += 1
        percent = data["scores"]/(len(questions)) * 100
    bot.delete_state(callback.from_user.id, callback.message.chat.id)
    result(callback, int(percent))


@bot.callback_query_handler(state=attributes[f"Question{len(questions)}"], func=lambda callback: callback.data == "bad")
def bad_answer_final(callback: telebot.types.CallbackQuery):
    bot.send_message(callback.message.chat.id, f"Хммм... Немного не так.\nПравильный ответ: {get_answers_current(len(questions)-1)[2]}.")
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        percent = data["scores"]/(len(questions)) * 100
    bot.delete_state(callback.from_user.id, callback.message.chat.id)
    result(callback, int(percent))


@bot.callback_query_handler(func=lambda callback: True)
def answer(callback: telebot.types.CallbackQuery):
    current_state = get_last_chislo_in_str(str(bot.get_state(callback.from_user.id, callback.message.chat.id))) #возвращает число, находящееся в конце строки "Questinon{n}"
    if callback.data == 'good':
        get_good(callback)
    else:
        get_bad(callback, current_state)
    bot.set_state(callback.from_user.id, attributes[f"Question{current_state+1}"], callback.message.chat.id)
    get_question(callback, current_state)