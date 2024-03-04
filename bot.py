import logging
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_name = (await context.bot.get_me()).first_name
    user_name = update.effective_user.first_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hey, {user_name} my name is {bot_name}.")


if __name__ == '__main__':
    app = ApplicationBuilder().token(os.environ['TOKEN']).build()
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)
    app.run_polling()
