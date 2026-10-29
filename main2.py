# import asyncio
# import logging
# from aiogram import F
# from aiogram.types import Message
# from aiogram import Bot, Dispatcher
# from aiogram.filters import CommandStart, Command


# BOT_TOKEN = "8910026319:AAFnWGTRBEZt6KgINt0GZxeOD3Q-XbY0qgg"


# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()   #


# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer(
#         f"Привет,{message.from_user.full_name} я твой бот!"
#     )
#     print(f"Пользователь {message.from_user.full_name} написал /start!")

# @dp.message(Command("help"))
# async def cmd_help(message: Message):
#     await message.answer(
#         "/start - команда для запуска\n"
#         "/help - список команд"
#     )

# @dp.message(F.text.lower() == "группа")
# async def cmd_group(message: Message):
#     await message.answer("Твоя группа 71-1!")


# # @dp.message(F.from_user.id == 8327876817)
# # async def cmd_group(message: Message):
# #     await message.answer("привет шеф!")


# @dp.message()
# async def echo(message: Message):
#     await message.answer(f"Ты написал: {message.text}")

# async def main():
#     await dp.start_polling(bot) 


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     asyncio.run(main())