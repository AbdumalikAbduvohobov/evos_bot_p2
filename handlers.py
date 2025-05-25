from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from database import database
from keyboards import select_language, start_buttons
from messages import messages, job_info

router = Router()


@router.message(F.text.in_(["🇺🇿/🇷🇺 Til", "🇺🇿/🇷🇺 Язык"]))
async def get_language(message: Message):
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(messages[lang]['select_lang'], reply_markup=select_language())

@router.callback_query(F.data.in_(["uz", "ru"]))
async def set_language(callback_query: CallbackQuery):
    lang = callback_query.data
    database.set_user_lang(telegram_id=callback_query.from_user.id, lang=lang)
    await callback_query.message.answer(text='Hello', reply_markup=start_buttons(lang))

@router.message(F.text.in_(["Вакансии", "Bo'sh ish o'rinlari"]))
async def get_jobs(message: Message):
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(text=job_info[lang]["job_position"])