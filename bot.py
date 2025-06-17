import telegram
from flask import Flask, request

app = Flask(__name__)

TOKEN = "your_token_here"
CHAT_ID = "your_chat_id_here"

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', {}).get('text', '')
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=f"Received: {message}")
    return 'ok'

if __name__ == '__main__':
    app.run()