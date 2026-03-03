from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler, \
    filters, PicklePersistence

from config import config
from keyboards import REPLY_KEYBOARD, get_keyboard

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт, друже!", reply_markup=get_keyboard())


async def answer_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "Кнопка 1":
        await update.message.reply_text("Ви натиснули кнопку 1")
    else:
        await update.message.reply_text("Ви натиснули кнопку 2")


async def remove_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Клавіатуру очищено", reply_markup=ReplyKeyboardRemove())


async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = context.args[0] if context.args else None

    if not password:
        await update.message.reply_text("Введіть пароль")
        return

    if password == config.admin_password:
        await update.message.reply_text("Доступ надано")
        context.user_data["is_admin"] = True
    else:
        await update.message.reply_text("Неправильний пароль")
        

async def get_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("is_admin"):
        await answer_chat_info(update, context, ">>>")
    else:
        await update.message.reply_text("Потрібен доступ")


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query.data == "like":
        await update.effective_chat.send_message("Дякуємо за лайк!")
    elif query.data == "dislike":
        await query.edit_message_text("Отримано дизлайк!")

    await query.answer()


async def answer_chat_info(update: Update, context: ContextTypes.DEFAULT_TYPE, prefix: str = ""):
    chat = update.effective_chat
    info = f"{prefix}Chat ID: {chat.id}, Type: {chat.type}"
    await context.bot.send_message(chat_id=chat.id, text=info)


BOT_COMMANDS = [
        ("start", "Початок роботи — вітання та головне меню"),
        ("cancel", "Скасувати поточну дію"),
        ("help", "Отримати допомогу по боту"),
]

def main():
    async def post_init_func(app):
        await app.bot.set_my_commands(BOT_COMMANDS)

    persistence = PicklePersistence(filepath="my_bot_data.pickle")

    application = (
        ApplicationBuilder()
        .token(config.token)
        .post_init(post_init_func)
        .persistence(persistence)
        .build()
    )

    application.add_handler(CommandHandler("start", start_func))
    application.add_handler(CommandHandler("login", login))
    application.add_handler(CommandHandler("get_data", get_data))

    application.add_handler(MessageHandler(filters.Text(("Кнопка 1", "Кнопка 2")), answer_buttons))
    application.add_handler(MessageHandler(filters.Text(("Прибрати клавіатуру",)), remove_keyboard))

    application.add_handler(CallbackQueryHandler(callback_handler))

    print("Бота запущено...")
    application.run_polling()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Бота зупиненно")

