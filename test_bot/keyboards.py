from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, constants


REPLY_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Кнопка 1"), KeyboardButton("Кнопка 2")],
        [KeyboardButton("Прибрати клавіатуру")]
    ],
    resize_keyboard=True
)

def get_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Лайк 👍", callback_data="like"),
            InlineKeyboardButton("Дизлайк 👎", callback_data="dislike"),
        ],
        [InlineKeyboardButton("Детальніше →", url="https://core.telegram.org/bots/api")],
    ])
