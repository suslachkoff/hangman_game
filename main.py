import telebot
import random

# Укажите токен вашего бота
TOKEN = '5894098532:AAGOr_Hj2VSAbCRtrFON6Bg36kuexi9tqXo'

# Список слов для игры
words = ['лето', 'солнце', 'тепло']

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я бот для игры в угадывание слова. Чтобы начать игру, введите /play.')

# Обработчик команды /play
@bot.message_handler(commands=['play'])
def play_game(message):
    # Выбираем случайное слово из списка
    word = random.choice(words)
    # Создаем список из букв слова и заменяем их на символ "_"
    hidden_word = list('_' * len(word))
    # Отправляем сообщение с загаданным словом
    bot.reply_to(message, f"Я загадал слово из {len(word)} букв: {' '.join(hidden_word)}. Введите букву:")

    guesses_left = 8

    # Обработчик сообщений с буквами
    @bot.message_handler(func=lambda message: message.text.isalpha())
    def guess_letter(message):
        nonlocal hidden_word
        nonlocal word
        nonlocal guesses_left

        # Если буква уже угадана, просим ввести другую
        if message.text in hidden_word:
            bot.reply_to(message, f"Вы уже угадали букву {message.text}. Введите другую:")
            return

        # Если буква есть в слове, заменяем соответствующий символ "_"
        if message.text in word:
            for i in range(len(word)):
                if word[i] == message.text:
                    hidden_word[i] = message.text

            # Если все буквы угаданы, завершаем игру
            if '_' not in hidden_word:
                bot.reply_to(message, f"Вы выиграли! Загаданное слово было '{word}'.")
                return

            # Иначе просим ввести следующую букву
            bot.reply_to(message, f"Вы угадали букву {message.text}. Текущее состояние слова: {' '.join(hidden_word)}. Введите следующую букву:")

        # Если буквы нет в слове, сообщаем об этом и просим ввести следующую букву
        else:
            guesses_left -= 1
            if guesses_left == 0:
                bot.reply_to(message, f"Вы проиграли! Загаданное слово было '{word}'. Начинаем игру заново.")
                play_game(message)
                return

            bot.reply_to(message, f"Буква {message.text} не входит в загаданное слово. Осталось попыток: {guesses_left}. Введите следующую букву:")

    # Запускаем обработчик сообщений с буквами
bot.polling(none_stop=True)