import os
import telegram
from telegram import InputFile

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = telegram.Bot(token=BOT_TOKEN)

def send_message():
    bot.send_message(chat_id=CHAT_ID, text="Тестовое сообщение от зрелого трейдера")

if __name__ == "__main__":
    send_message()
