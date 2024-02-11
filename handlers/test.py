import telebot.types

from telebot.handler_backends import StatesGroup, State

from handlers.funcs import get_question, get_good, get_bad, result, get_answers_current, questions
from init_bot import bot


class Questions(StatesGroup):
    # states = []                         Так не работает почему-то :(
    # for i in range(len(questions)):
    #     states.append(State())
    Question1 = State()
    Question2 = State()
    Question3 = State()
    Question4 = State()
    Question5 = State()
    Question6 = State()
    Question7 = State()
    Question8 = State()
    Question9 = State()
    Question10 = State()
    Question11 = State()
    Question12 = State()
    Question13 = State()
    Question14 = State()

#дальше копипаст... что только не пробовал, никак не получилось сделать эффективнее

@bot.callback_query_handler(func=lambda callback: callback.data == "start")
def question1(callback: telebot.types.CallbackQuery):
    bot.set_state(callback.from_user.id, Questions.Question1, callback.message.chat.id)
    get_question(callback, 0)
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        data["scores"] = 0


@bot.callback_query_handler(state=Questions.Question1, func=lambda callback: callback.data == "good")
def good_answer1(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question2, callback.message.chat.id)
    get_question(callback, 1)


@bot.callback_query_handler(state=Questions.Question1, func=lambda callback: callback.data == "bad")
def bad_answer1(callback: telebot.types.CallbackQuery):
    get_bad(callback, 1)
    bot.set_state(callback.from_user.id, Questions.Question2, callback.message.chat.id)
    get_question(callback, 1)


@bot.callback_query_handler(state=Questions.Question2, func=lambda callback: callback.data == "good")
def good_answer2(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question3, callback.message.chat.id)
    get_question(callback, 2)


@bot.callback_query_handler(state=Questions.Question2, func=lambda callback: callback.data == "bad")
def bad_answer2(callback: telebot.types.CallbackQuery):
    get_bad(callback, 2)
    bot.set_state(callback.from_user.id, Questions.Question3, callback.message.chat.id)
    get_question(callback, 2)


@bot.callback_query_handler(state=Questions.Question3, func=lambda callback: callback.data == "good")
def good_answer3(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question4, callback.message.chat.id)
    get_question(callback, 3)


@bot.callback_query_handler(state=Questions.Question3, func=lambda callback: callback.data == "bad")
def bad_answer3(callback: telebot.types.CallbackQuery):
    get_bad(callback, 3)
    bot.set_state(callback.from_user.id, Questions.Question4, callback.message.chat.id)
    get_question(callback, 3)


@bot.callback_query_handler(state=Questions.Question4, func=lambda callback: callback.data == "good")
def good_answer4(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question5, callback.message.chat.id)
    get_question(callback, 4)


@bot.callback_query_handler(state=Questions.Question4, func=lambda callback: callback.data == "bad")
def bad_answer4(callback: telebot.types.CallbackQuery):
    get_bad(callback, 4)
    bot.set_state(callback.from_user.id, Questions.Question5, callback.message.chat.id)
    get_question(callback, 4)


@bot.callback_query_handler(state=Questions.Question5, func=lambda callback: callback.data == "good")
def good_answer5(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question6, callback.message.chat.id)
    get_question(callback, 5)


@bot.callback_query_handler(state=Questions.Question5, func=lambda callback: callback.data == "bad")
def bad_answer5(callback: telebot.types.CallbackQuery):
    get_bad(callback, 5)
    bot.set_state(callback.from_user.id, Questions.Question6, callback.message.chat.id)
    get_question(callback, 5)


@bot.callback_query_handler(state=Questions.Question6, func=lambda callback: callback.data == "good")
def good_answer6(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question7, callback.message.chat.id)
    get_question(callback, 6)


@bot.callback_query_handler(state=Questions.Question6, func=lambda callback: callback.data == "bad")
def bad_answer6(callback: telebot.types.CallbackQuery):
    get_bad(callback, 6)
    bot.set_state(callback.from_user.id, Questions.Question7, callback.message.chat.id)
    get_question(callback, 6)


@bot.callback_query_handler(state=Questions.Question7, func=lambda callback: callback.data == "good")
def good_answer7(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question8, callback.message.chat.id)
    get_question(callback, 7)


@bot.callback_query_handler(state=Questions.Question7, func=lambda callback: callback.data == "bad")
def bad_answer7(callback: telebot.types.CallbackQuery):
    get_bad(callback, 7)
    bot.set_state(callback.from_user.id, Questions.Question8, callback.message.chat.id)
    get_question(callback, 7)


@bot.callback_query_handler(state=Questions.Question8, func=lambda callback: callback.data == "good")
def good_answer8(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question9, callback.message.chat.id)
    get_question(callback, 8)


@bot.callback_query_handler(state=Questions.Question8, func=lambda callback: callback.data == "bad")
def bad_answer8(callback: telebot.types.CallbackQuery):
    get_bad(callback, 8)
    bot.set_state(callback.from_user.id, Questions.Question9, callback.message.chat.id)
    get_question(callback, 8)


@bot.callback_query_handler(state=Questions.Question9, func=lambda callback: callback.data == "good")
def good_answer9(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question10, callback.message.chat.id)
    get_question(callback, 9)


@bot.callback_query_handler(state=Questions.Question9, func=lambda callback: callback.data == "bad")
def bad_answer9(callback: telebot.types.CallbackQuery):
    get_bad(callback, 9)
    bot.set_state(callback.from_user.id, Questions.Question10, callback.message.chat.id)
    get_question(callback, 9)


@bot.callback_query_handler(state=Questions.Question10, func=lambda callback: callback.data == "good")
def good_answer10(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question11, callback.message.chat.id)
    get_question(callback, 10)


@bot.callback_query_handler(state=Questions.Question10, func=lambda callback: callback.data == "bad")
def bad_answer10(callback: telebot.types.CallbackQuery):
    get_bad(callback, 10)
    bot.set_state(callback.from_user.id, Questions.Question11, callback.message.chat.id)
    get_question(callback, 10)


@bot.callback_query_handler(state=Questions.Question11, func=lambda callback: callback.data == "good")
def good_answer11(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question12, callback.message.chat.id)
    get_question(callback, 11)


@bot.callback_query_handler(state=Questions.Question11, func=lambda callback: callback.data == "bad")
def bad_answer11(callback: telebot.types.CallbackQuery):
    get_bad(callback, 11)
    bot.set_state(callback.from_user.id, Questions.Question12, callback.message.chat.id)
    get_question(callback, 11)


@bot.callback_query_handler(state=Questions.Question12, func=lambda callback: callback.data == "good")
def good_answer12(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question13, callback.message.chat.id)
    get_question(callback, 12)


@bot.callback_query_handler(state=Questions.Question12, func=lambda callback: callback.data == "bad")
def bad_answer12(callback: telebot.types.CallbackQuery):
    get_bad(callback, 12)
    bot.set_state(callback.from_user.id, Questions.Question13, callback.message.chat.id)
    get_question(callback, 12)


@bot.callback_query_handler(state=Questions.Question13, func=lambda callback: callback.data == "good")
def good_answer13(callback: telebot.types.CallbackQuery):
    get_good(callback)
    bot.set_state(callback.from_user.id, Questions.Question14, callback.message.chat.id)
    get_question(callback, 13)


@bot.callback_query_handler(state=Questions.Question13, func=lambda callback: callback.data == "bad")
def bad_answer13(callback: telebot.types.CallbackQuery):
    get_bad(callback, 13)
    bot.set_state(callback.from_user.id, Questions.Question14, callback.message.chat.id)
    get_question(callback, 13)


@bot.callback_query_handler(state=Questions.Question14, func=lambda callback: callback.data == "good")
def good_answer14(callback: telebot.types.CallbackQuery):
    bot.send_message(callback.message.chat.id, "Молодец! Верно")
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        data["scores"] += 1
        percent = data["scores"]/len(questions) * 100
    bot.delete_state(callback.from_user.id, callback.message.chat.id)
    result(callback, percent)


@bot.callback_query_handler(state=Questions.Question14, func=lambda callback: callback.data == "bad")
def bad_answer14(callback: telebot.types.CallbackQuery):
    bot.send_message(callback.message.chat.id, f"Хммм... Немного не так.\nПравильный ответ: {get_answers_current(13)[2]}.")
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        percent = data["scores"]/(len(questions)-1) * 100
    bot.delete_state(callback.from_user.id, callback.message.chat.id)
    result(callback, int(percent))

