from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from data.config import ADMIN

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    user_id = message.chat.id
    user_fullname = message.chat.full_name
    message_text = message.text
    
    if str(user_id) == ADMIN[0]:
        status = message.reply_to_message
        if status:
            send_user_id = message.reply_to_message.text.split(',')[0].split(':')[1]
            await bot.send_message(int(send_user_id), f'Ответ админа на ваш вопрос: {message_text}') 
            await message.answer("Спасибо за ваш ответ")
        else:
            await message.answer("Вы не можете задать вопрос самому себе! Вы являетесь админом! Ответьте на сообщение!")
    else:
        await bot.send_message(ADMIN[0], f'ID:{user_id}, Пользователь {user_fullname} написал вам сообщение! Ответьте в этом чате! Текст: {message_text}')
        await message.answer(f"Ваше сообщение отправлено админу, ждите:\n"
                            f"{message.text}")

# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
