import telebot

TOKEN = '5894098532:AAGOr_Hj2VSAbCRtrFON6Bg36kuexi9tqXo'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я бот для игры в угадывание слова, или же "Виселица". Чтобы начать игру, введите /play.')

bot.polling(none_stop=True)
