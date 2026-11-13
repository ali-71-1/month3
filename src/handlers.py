from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from src.state import Quiz, UserStates
from src.question import QUESTIONS
from src.keyboards import reply_buttons, inline_buttons, inline_buttons2, inline_buttons3
from db.users import get_user, create_user, update_user_username, delete_user
from db.questions import get_all_questions
from db.results import save_result
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username or "Аноним"
    )
    await message.answer(
        f"Привет,{message.from_user.full_name} я твой бот! \n Вот твой результат который возвращается из базы данных: \n{user}",
        reply_markup=reply_buttons
    )
    print(f"Пользователь {message.from_user.full_name} написал /start!")

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start - команда для запуска\n"
        "/help - список команд\n"
        "/update_username - обновить имя пользователя\n"
        "/delete_account - удалить аккаунт",
        reply_markup=inline_buttons
    )

@router.message(Command("update_username"))
async def cmd_update_username(message: Message, state: FSMContext):
    await state.set_state(UserStates.waiting_new_username)
    await message.answer("Введите новое имя пользователя:")

@router.message(UserStates.waiting_new_username)
async def process_new_username(message: Message, state: FSMContext):
    new_username = message.text
    telegram_id = message.from_user.id
    update_user_username(telegram_id, new_username)
    await state.clear()
    await message.answer(f"Твое новое имя пользователя обновлено на: {new_username}")
    print(f"Пользователь {message.from_user.full_name} обновил имя на {new_username}")

@router.message(Command("delete_account"))
async def cmd_delete_account(message: Message):
    telegram_id = message.from_user.id
    delete_user(telegram_id)
    await message.answer("Твой аккаунт был удален из базы данных. Отправь /start для регистрации заново.")
    print(f"Пользователь {message.from_user.full_name} удалил свой аккаунт!")

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
async def cmd_group_actions(message: Message):
    await message.answer("На данный момент акций нет(")
    print(f"Пользователь {message.from_user.full_name} написал Акции!")

@router.message(F.text == "Каталог")
async def cmd_group_catalog(message: Message):
    await message.answer("На данный момент каталог пуст(")
    print(f"Пользователь {message.from_user.full_name} написал Каталог!")

@router.message(F.text == "Контакты")
async def cmd_group_contacts(message: Message):
    await message.answer("Наши контакты: +996 555 55 55 55")
    print(f"Пользователь {message.from_user.full_name} написал Контакты!")

@router.message(F.text == "номер администратора")
async def cmd_group_admin(message: Message):
    await message.answer("Номер администратора: +996 777 77 77 77")
    print(f"Пользователь {message.from_user.full_name} написал номер администратора!")

@router.message(F.text == "флаги")
async def cmd_group_flags(message: Message):
    await message.answer("Флаги: 🇰🇬 🇺🇸 🇷🇺")
    print(f"Пользователь {message.from_user.full_name} написал флаги!")
    return await message.answer("Больше флагов: ", reply_markup=inline_buttons3)

@router.callback_query(F.data == "quiz_start")
async def quiz_start(callbak: CallbackQuery, state: FSMContext):
    await callbak.answer("Начинаем игру!", show_alert=True)
    questions = get_all_questions()
    if not questions:
        await callbak.message.answer("Вопросы не найдены в базе данных.")
        return


    await state.update_data(question=questions, index=0, score=0)
    await state.set_state(Quiz.waiting_abswer)
    await callbak.message.answer(f"Вопрос 1: {questions[0]['question_text']}")

@router.message(Quiz.waiting_abswer)
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    score = data["score"]
    questions = data["question"]
    user = get_user(telegram_id=message.from_user.id)
    q = questions[index]
    is_correct = message.text.lower() == q["correct_answer"].lower()
    save_result(users_id=user["id"],
                question_id=q["id"],
                is_correct=is_correct
                   )

    if is_correct:
        score += 1
        await message.answer("Правильно! +1")
    else:
        await message.answer(f"Неверно. Правильный ответ: {q['correct_answer']}")

    index += 1
    if index >= len(questions):
        await message.answer(f"Конец! Счет: {score} / {len(questions)}")
        await state.clear()
        await message.answer("Хочешь сыграть снова?", reply_markup=inline_buttons2)
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"Вопрос {index + 1}: {questions[index]['question_text']}")

@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.from_username}, {message.text}")