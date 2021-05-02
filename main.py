from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler

from wiki import search_wiki
# Максим Соловов

TOKEN = "1505183260:AAGwx97VADlg30kIOFBGqqEfKHRjzNf1miI"

def echo(update, context):
    txt = update.message.text
    if txt.lower() in ['привет','здаров','hello']:
        txt = "И тебе привет аналоговый друг!"
    update.message.reply_text(txt)

def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь")

def help(update, context):
    update.message.reply_text(
        "/wiki <запрос> - поиск в википедии")

def wiki(update, context):
    print(context.args)
    word = ' '.join(context.args)
    if word:
        update.message.reply_text("Идет поиск...")
        response, url = search_wiki(word)
        update.message.reply_text(response+url)
    else:
        update.message.reply_text("Необходимо ввести что искать")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен...")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("wiki", wiki))
    dp.add_handler(MessageHandler(Filters.text, echo))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    # Ждём завершения приложения.
    updater.idle()

main()
