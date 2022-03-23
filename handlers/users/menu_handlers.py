from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from utils.db_api.database import data_text
from keyboards.inline.menu_keyboards import *

from utils.db_api.database import specialities_data, degrees_data, main_menu_data, questions_data, in_questions_data, data_text, kafedras

import logging

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    logging.info(f"id={message.from_user.id}, full_name={message.from_user.full_name}, locale={message.from_user.locale}, mention={message.from_user.mention}, username={message.from_user.username}")

    await list_of_degrees(message)

async def list_of_degrees(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await degrees_keyboard()

    if isinstance(message, types.Message):
        await message.answer(f"{message['from']['first_name']}, пожалуйста выберите степень на которой вы обучаетесь:", reply_markup=markup)
    
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)

async def list_of_specialities(callback: Union[types.Message, types.CallbackQuery], degrees, **kwargs):
    markup = await specialities_keyboard(degrees)
    await callback.message.edit_text(text = "Пожалуйста выберите специальность на которой вы обучаетесь:")
    await callback.message.edit_reply_markup(markup)

async def list_of_mainmenu(callback: Union[types.Message, types.CallbackQuery], degrees, specialities, **kwargs):
    main_text = f"Вы выбрали {degrees_data[degrees]} - {specialities_data[degrees][specialities]} \n\n"
    markup = await main_menu_keyboard(degrees, specialities)
    await callback.message.edit_text(text = main_text+"Пожалуйста выберите вопрос:")
    await callback.message.edit_reply_markup(markup)

async def list_of_questions(callback: types.CallbackQuery, degrees, specialities, main_menu, **kwargs):
    main_text = f"Вы выбрали {degrees_data[degrees]} - {specialities_data[degrees][specialities]} \n\n"
    if main_menu in ['3_mm', '4_mm', '5_mm', '6_mm', '7_mm']:
        markup = await questions_keyboard(degrees, specialities, main_menu)
        await callback.message.edit_text(main_text)
        await callback.message.edit_reply_markup(markup)
    elif main_menu == "1_mm":
        kafedra_code = data_text[main_menu][degrees][specialities]
        show_data_text = kafedras[kafedra_code]
        markup = await questions_keyboard(degrees, specialities, main_menu)
        await callback.message.edit_text(main_text+show_data_text, reply_markup=markup, parse_mode="HTML")
    
    else:
        
        show_data_text = data_text[main_menu]
        markup = await questions_keyboard(degrees, specialities, main_menu)
        await callback.message.edit_text(main_text+show_data_text, reply_markup=markup, parse_mode="HTML")
        chat_id = callback.message['chat']['id']
        if main_menu == "10_mm":
            await bot.send_document(chat_id = chat_id, document = open('files/documents/Заявление на место в общежитии.pdf', 'rb'))
        


async def list_of_in_questions(callback: types.CallbackQuery, degrees, specialities, main_menu, questions, **kwargs):
    main_text = f"Вы выбрали {degrees_data[degrees]} - {specialities_data[degrees][specialities]} \n\n"
    if questions in ["6_qd", "7_qd"]:
        markup = await in_questions_keyboard(degrees, specialities, main_menu, questions)
        await callback.message.edit_text(main_text, parse_mode="HTML")
        await callback.message.edit_reply_markup(markup)
    else:
        show_data_text = data_text[questions]
        markup = await in_questions_keyboard(degrees, specialities, main_menu, questions)
        await callback.message.edit_text(main_text+show_data_text, reply_markup=markup, parse_mode="HTML")
        chat_id = callback.message['chat']['id']
        if questions == "9_qd":
            await bot.send_document(chat_id = chat_id, document = open('files/documents/Форма заявления Кульдеев Е.И.каз.pdf', 'rb'))
            await bot.send_document(chat_id = chat_id, document = open('files/documents/Формы заявлений Кульдеев Е.И. русc.pdf', 'rb'))
        elif questions == "5_qd":
            await bot.send_document(chat_id = chat_id, document = open('files/documents/Пример заполнения каз.pdf', 'rb'))
            await bot.send_document(chat_id = chat_id, document = open('files/documents/Пример заполнения русс.pdf', 'rb'))
            
async def show_question(callback: types.CallbackQuery, degrees, specialities, main_menu, questions, in_questions, question_id):
    main_text = f"Вы выбрали {degrees_data[degrees]} - {specialities_data[degrees][specialities]} \n\n"
    markup = question_id_keyboard_back(degrees, specialities, main_menu, questions, in_questions, question_id)
    show_data_text = data_text[questions][in_questions]
    chat_id = callback.message['chat']['id']
    if in_questions in ["1_iqd", "2_iqd", "3_iqd", "4_iqd"]:
        await bot.send_document(chat_id = chat_id, document = open('files/documents/Форма заявления Жаутиков Б.A русс.pdf', 'rb'))
        await bot.send_document(chat_id = chat_id, document = open('files/documents/Форма Заявления Жаутиков Б.A.pdf', 'rb'))
        
    await callback.message.edit_text(main_text + show_data_text, reply_markup=markup, parse_mode="HTML")



@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    degrees = callback_data.get('degrees')
    specialities = callback_data.get('specialities')
    main_menu = callback_data.get('main_menu')
    questions = callback_data.get('questions')
    in_questions = callback_data.get('in_questions')
    question_id = callback_data.get('question_id')

    levels = {
        "0": list_of_degrees,
        "1": list_of_specialities,
        "2": list_of_mainmenu,
        "3": list_of_questions,
        "4": list_of_in_questions,
        "5": show_question
    
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        degrees = degrees,
        specialities = specialities,
        main_menu = main_menu,
        questions = questions,
        in_questions = in_questions,
        question_id = question_id
    )