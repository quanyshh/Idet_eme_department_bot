from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.database import specialities_data, degrees_data, main_menu_data, questions_data, in_questions_data
menu_cd = CallbackData("show_menu", "level", "degrees", "specialities", "main_menu", "questions", "in_questions", "question_id")

def make_callback_data(level, degrees="0", specialities="0", main_menu="0", questions="0", in_questions="0", question_id="0"):
    return menu_cd.new(level = level, 
                        degrees = degrees, 
                        specialities = specialities, 
                        main_menu =main_menu, 
                        questions = questions,
                        in_questions = in_questions,
                        question_id = question_id
    )

async def degrees_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)

    for key, value in degrees_data.items():
        button_text = value.upper()
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, degrees = key)
        
        markup.insert(
            InlineKeyboardMarkup(text = button_text, callback_data = callback_data)
        )

    return markup

async def specialities_keyboard(degrees):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1)

    for key, value in specialities_data[degrees].items():
        button_text = value
        callback_data = make_callback_data(level = CURRENT_LEVEL + 1, degrees = degrees, specialities = key)

        markup.insert(
            InlineKeyboardButton(text = button_text, callback_data = callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data = make_callback_data(level = CURRENT_LEVEL - 1, degrees = degrees)
        )
    )

    return markup

async def main_menu_keyboard(degrees, specialities):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)

    for key, value in main_menu_data.items():
        button_text = value
        callback_data = make_callback_data(level = CURRENT_LEVEL + 1,
                                            degrees = degrees,
                                            specialities = specialities,
                                            main_menu = key
        )

        markup.insert(
            InlineKeyboardButton(text = button_text, callback_data = callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data = make_callback_data(
                level = CURRENT_LEVEL - 1, 
                degrees = degrees, 
                specialities = specialities
            )
        )
    )

    return markup

async def questions_keyboard(degrees, specialities, main_menu):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup(row_width=1)

    try:
        for key, value in questions_data[main_menu].items():
            button_text = value
            callback_data = make_callback_data(
                level = CURRENT_LEVEL + 1, 
                degrees = degrees, 
                specialities = specialities,
                main_menu = main_menu,
                questions = key
            )

            markup.insert(
                InlineKeyboardButton(text = button_text, callback_data = callback_data)
            )

        markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data = make_callback_data(
                level = CURRENT_LEVEL - 1, 
                degrees = degrees, 
                specialities = specialities,
                main_menu = main_menu
            )
        )
    )
    except Exception as e:
        
        markup.row(
            InlineKeyboardButton(
                text="Назад", 
                callback_data = make_callback_data(
                    level = CURRENT_LEVEL-1, 
                    degrees = degrees, 
                    specialities= specialities,
                    main_menu=main_menu
                )
            )
        )

    return markup

async def in_questions_keyboard(degrees, specialities, main_menu_btn, questions):
    CURRENT_LEVEL = 4
    markup = InlineKeyboardMarkup(row_width=1)

    try:
        for key, value in in_questions_data[questions].items():
            button_text = value
            callback_data = make_callback_data(
                level = CURRENT_LEVEL + 1, 
                degrees = degrees, 
                specialities = specialities,
                main_menu = main_menu_btn,
                questions = questions,
                in_questions = key
            )

            markup.insert(
                InlineKeyboardButton(text = button_text, callback_data = callback_data)
            )

        markup.row(
            InlineKeyboardButton(
                text = "Назад",
                callback_data = make_callback_data(
                    level = CURRENT_LEVEL - 1, 
                    degrees = degrees, 
                    specialities = specialities,
                    main_menu = main_menu_btn,
                    questions = questions
                )
            )
        )

    except Exception as e:
        markup.row(
            InlineKeyboardButton(
                text = "Назад",
                callback_data = make_callback_data(
                    level = CURRENT_LEVEL - 1, 
                    degrees = degrees, 
                    specialities = specialities,
                    main_menu = main_menu_btn,
                    questions = questions
                )
            )
        )

    return markup

def question_id_keyboard_back(degrees, specialities, main_menu, questions, in_questions, question_id):
    CURRENT_LEVEL = 5
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад", 
            callback_data = make_callback_data(
                level = CURRENT_LEVEL-1, 
                degrees = degrees, 
                specialities= specialities,
                main_menu=main_menu,
                questions=questions,
                in_questions = in_questions,
                question_id = question_id
            )
        )
    )

    return markup