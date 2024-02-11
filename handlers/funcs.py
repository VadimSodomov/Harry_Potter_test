import telebot

from init_bot import bot


with open("handlers/questions.txt", encoding="utf-8") as file:
    questions = file.read().split("\n")

with open("handlers/answers.txt", encoding="utf-8") as file:
    answers = file.read().split("\n")


def get_question(callback: telebot.types.CallbackQuery, question_number):
    bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id, reply_markup=None)
    text = questions[question_number]
    ans = get_answers_current(question_number)
    answer_variants = ans[1]
    answer_good = ans[2]
    d = {}
    for answer in answer_variants:
        if answer == answer_good:
            d[answer] = {"callback_data": "good"}
        else:
            d[answer] = {"callback_data": "bad"}
    markup = telebot.util.quick_markup(d)
    with open(f"handlers/photo/{question_number + 1}.webp", "rb") as photo:
        bot.send_photo(callback.message.chat.id, photo, reply_markup=markup, caption=text)


def get_good(callback):
    bot.send_message(callback.message.chat.id, "Молодец! Верно) Перейдем к следующему вопросу.")
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        data["scores"] += 1


def get_bad(callback, next_question):
    bot.send_message(callback.message.chat.id, f"Хммм... Немного не так.\nПравильный ответ: {get_answers_current(next_question-1)[2]}.\nПерейдем к следующему вопросу.")


def get_answers_current(question_number):
    answers_current = answers[question_number].split(" $ ")  # [все варианты ответов, правильный]
    answer_variants = answers_current[0].split(", ")  # все варинанты ответов [..., ..., ...]
    answer_good = answers_current[1]
    return [answers_current, answer_variants, answer_good]


def result(callback: telebot.types.CallbackQuery, percent):
    if percent < 60:
        with open("handlers/photo/photo_result/bad.jpg", "rb") as photo:
            bot.send_photo(callback.message.chat.id, photo, caption=f"{percent}/{100}\n\nСпасибо за прохождение теста! \n\nРезультаты могли быть и лучше. Думаю, тебе стоит пересмотреть или перечитать Вселенную Гарри Поттера и восполнить некоторые забытые моменты)")
    elif percent < 75:
        with open("handlers/photo/photo_result/good.jpg", "rb") as photo:
            bot.send_photo(callback.message.chat.id, photo, caption=f"{percent}/{100}\n\nСпасибо за прохождение теста! \n\nТы неплохо знаешь Вселенную Гарри Поттера, но, думаю, если посмотришь фильмы или почитаешь книгу, то некоторые забытые моменты восполнятся, и ты сможешь пройти тест на еще более высокие результаты)")
    elif percent < 90:
        with open("handlers/photo/photo_result/very_good.jpg", "rb") as photo:
            bot.send_photo(callback.message.chat.id, photo, caption=f"{percent}/{100}\n\nСпасибо за прохождение теста! \n\nТы хорошо владеешь знаниями Вселенной Гарри Поттера! Есть пара забытых моментов, но, думаю, просмотр этих атмосферных фильмов на выходных это поправят)")
    else:
        with open("handlers/photo/photo_result/the_best.jpg", "rb") as photo:
            bot.send_photo(callback.message.chat.id, photo, caption=f"{percent}/{100}\n\nСпасибо за прохождение теста! \n\nТы молодец, замечательно разбираешься во Вселенной Гарри Поттера) Думаю, ты настоящий поттероман!")
        magic_gift(callback)


def magic_gift(callback: telebot.types.CallbackQuery):
    with open("handlers/photo/photo_result/magic_gift.jpg", "rb") as photo:
        bot.send_photo(callback.message.chat.id, photo, caption=f"Держи, она выбрала тебя!")