from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton
                           )


reply_buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Корзина"), KeyboardButton(text="Акции")],
    [KeyboardButton(text="Каталог"), KeyboardButton(text="Контакты")],
    [KeyboardButton(text="номер администратора"), KeyboardButton(text="флаги")]
], resize_keyboard=True, input_field_placeholder="Выберите пункт")

inline_buttons3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Кыргызтан", url="https://www.megaflag.ru/information/spravochnaya-informaciya/flagi-stran?srsltid=AYCX9vJlgfA_C3QDfBw-tQ7m8l0uw221bt-N8BCb32ENe418jP_MsA35")],
])

inline_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"), InlineKeyboardButton(text="Начать игру", callback_data="quiz_start")]
])


inline_buttons2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Играть снова", callback_data="quiz_start")]
])