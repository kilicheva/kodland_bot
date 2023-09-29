from telegram import Bot, Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes, filters
from credits import bot_token
from googletrans import Translator

import string


class Translator_dict:
    # Инициализация объекта(конструктор)
    def __init__(self, word='program'):
        # Поля или атрибуты класса
        self.word = word
        # Экземпляр класса из библиотеки googletrans
        self.translator = Translator()

    # Метод класса
    def translate_text(self):
        if self.word[0].upper() in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='ru').text
            return translate_word
        elif self.word[0].upper() not in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='en').text
            return translate_word











class MyBot:
    # Инициализация объекта(конструктор)
    def __init__(self, bot_token)  -> None:

        self.application = Application.builder().token(bot_token).build()

        # Регистрируем обработчики команд
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help))

        # Регистрируем обработчик для текстовых сообщений
        # self.application.add_handler(MessageHandler(filters.text & ~filters.command, self.translate_text))

        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

    # Метод класса
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        print(user.mention_html())
        await update.message.reply_html(
            f"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    # async def translate_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #     word = update.message.text
    #     print(word)
    #     obj = Translator_dict(word)
    #     obj.translate_text()


    # Метод класса
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(text="Это простой бот. Он может отвечать на текстовые сообщения.")


if __name__ == "__main__":
    bot = MyBot(bot_token=bot_token)