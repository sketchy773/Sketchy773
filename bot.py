import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def handle_message(update, context):
    user_msg = update.message.text
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_msg}]
        )
        reply = res['choices'][0]['message']['content']
    except Exception as e:
        reply = "Error: " + str(e)
    update.message.reply_text(reply)

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()
