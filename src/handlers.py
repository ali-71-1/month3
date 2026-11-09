from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from src.state import Quiz
from src.question import QUESTIONS
from src.keyboards import reply_buttons, inline_buttons, inline_buttons2, inline_buttons3

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет,{message.from_user.full_name} я твой бот!",
        reply_markup=reply_buttons
    )
    print(f"Пользователь {message.from_user.full_name} написал /start!")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start - команда для запуска\n"
        "/help - список команд",
        reply_markup=inline_buttons
    )



@router.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "Этого бота создал Али. На данный момент бот ничего не умеет,но в дальнейшем здесь появится много крутых функции!"
    )
    print(f"Пользователь {message.from_user.full_name} написал /about!")


@router.message(F.text == "Корзина")
async def cmd_group(message: Message):
    await message.answer("Твоя корзина пуста(")
    print(f"Пользователь {message.from_user.full_name} написал Корзина!")
@router.message(F.text == "Акции")
async def cmd_group(message: Message):
    await message.answer("На данный момент акций нет(")
    print(f"Пользователь {message.from_user.full_name} написал Акции!")
@router.message(F.text == "Каталог")
async def cmd_group(message: Message):
    await message.answer("На данный момент каталог пуст(")
    print(f"Пользователь {message.from_user.full_name} написал Каталог!")
@router.message(F.text == "Контакты")
async def cmd_group(message: Message):
    await message.answer("Наши контакты: +996 555 55 55 55")
    print(f"Пользователь {message.from_user.full_name} написал Контакты!")

@router.message(F.text == "номер администратора")
async def cmd_group(message: Message):
    await message.answer("Номер администратора: +996 777 77 77 77")
    print(f"Пользователь {message.from_user.full_name} написал номер администратора!")

@router.message(F.text == "флаги")
async def cmd_group(message: Message):
    await message.answer("Флаги: 🇰🇬 🇺🇸 🇷🇺")
    return await message.answer("Больше флагов: ", reply_markup=inline_buttons3)
    print(f"Пользователь {message.from_user.full_name} написал флаги!")

@router.callback_query(F.data == "quiz_start")
async def quiz_start(callbak: CallbackQuery, state: FSMContext):
    await callbak.answer("Начинаем игру!", show_alert=True)
    await state.update_data(index=0, score=0)           #сохраняем прогресс 
    await state.set_state(Quiz.waiting_abswer)          #переводим состояние
    await callbak.message.answer(f"Вопрос 1: {QUESTIONS[0]["q"]}")


@router.message(Quiz.waiting_abswer)
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    score = data["score"]

    if message.text.lower() == QUESTIONS[index] ["a"]:
        score += 1
        await message.answer("Правильно! +1")
    else:
        await message.answer(f"Неверно. Правильный ответ: {QUESTIONS[index] ["a"]}")

    index += 1
    if index >= len(QUESTIONS):
        await message.answer(f"Конец! Счет: {score} / {len(QUESTIONS)}")
        await state.clear()
        await message.answer("Хочешь сыграть снова?", reply_markup=inline_buttons2)
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"Вопрос {index + 1}: {QUESTIONS[index]["q"]}")


@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")

