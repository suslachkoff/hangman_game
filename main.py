import telebot
import random

TOKEN = '5894098532:AAGOr_Hj2VSAbCRtrFON6Bg36kuexi9tqXo'

bot = telebot.TeleBot(TOKEN)

words = ['python', 'bot', 'hungmangame']

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я бот для игры в угадывание слова, или же "Виселица". Чтобы начать игру, введите /play.')

@bot.message_handler(commands=['play'])
def play_game(message):
    word = random.choice(words)
    bot.reply_to(message, f'Я загадал слово из {len(word)} букв. Это слово: {word}')

bot.polling(none_stop=True)