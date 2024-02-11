import telebot

from init_bot import bot


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text = "Привет! Здесь ты можешь узнать, насколько ты поттероман)\n" \
           "И поверь мне, всё не так просто, как кажется...\n"
    markup = telebot.util.quick_markup({
        "Начнем?": {"callback_data": "start"}
    })
    with open("handlers/img_start.jpeg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, text, reply_markup=markup)

