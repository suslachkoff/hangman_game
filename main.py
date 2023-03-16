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
    hidden_word = list('_' * len(word))
    bot.reply_to(message, f"Я загадал слово из {len(word)} букв. Это слово: {' '.join(hidden_word)}, а ответ: {word}. Введите букву:")

@bot.message_handler(func=lambda message: message.text.isalpha())
def guess_letter(message):
    global hidden_word
    if message.text in word:
        for i in range(len(word)):
            if word[i] == message.text:
                hidden_word[i] = message.text

    bot.reply_to(message, f"Вы угадали букву {message.text}. Текущее состояние слова: {' '.join(hidden_word)}. Введите следующую букву:")

    else:
        bot.reply_to(message, f"Буква {message.text} не входит в загаданное слово. Введите следующую букву:")

bot.polling(none_stop=True)