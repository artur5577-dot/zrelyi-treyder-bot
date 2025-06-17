import os
from flask import Flask, request
import telegram

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get("message", "📉 Сообщение по умолчанию от БАБЛО™")
    try:
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.ParseMode.HTML)
        return {'status': 'ok'}, 200
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
