from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("7199789473:AAF81VG0KjDgiS5mcIbW9ef7jpNnioxI5jQ")


@bot.message_handler(commands=["start","help"])
def start(message:Message):
    chat_id = message.chat.id
    name = message.from_user.full_name
    print(chat_id)
    bot.send_message(chat_id,f"Assalomu Alaykum {name}")


@bot.message_handler(content_types=["text","photo","video"])
def get_text(message:Message):
    chat_id = message.chat.id
    # text = message.text
    # bot.send_message(chat_id,text)
    bot.copy_message(-4137765248,chat_id,message.message_id)
    


bot.polling()

