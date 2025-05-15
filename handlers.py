import os

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from database import database
from keyboards import select_language, start_buttons
from messages import messages

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

@router.message(F.text == "🏢 Kampaniya haqida")
async def kampaniya(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    await message.answer_photo(caption = "Kompaniyamizning birinchi filiali 2006 yilda ochilgan bo’lib,"
                                         " shu kungacha muvaffaqiyatli faoliyat yuritib kelmoqdaligini bilarmidingiz? 15 yil davomida kompaniya avtobus bekatidagi kichik ovqatlanish joyidan zamonaviy,"
                                         " kengaytirilgan tarmoqqa aylandi, u bugungi kunda O‘zbekiston bo‘ylab 65 dan ortiq restoranlarni, o‘zining eng tezkor yetkazib berish xizmatini, zamonaviy IT-infratuzilmasini va 2000 dan ortiq xodimlarni o‘z ichiga oladi.",
                               photo = img)


@router.message(F.text == "Filialari")
async def filialari(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_1.png"))
    await message.answer_photo(caption = "Evos ochilgan nuqtalar", photo=img)

@router.message(F.text == "Menyu")
async def menyu(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_2.png"))
    await message.answer_photo(caption = "Bu Menyuda istalgan narsani topish mumkin", photo=img)

@router.message(F.text.in_(["Bo'sh ish o'rinlari", "Вакансии"]))
async def evos_jobs(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_4.png"))
    await message.answer_photo(caption = "Bo‘sh ish o‘rni: EVOS’da kuryer! 🚗🍔"
"Jamoamizga qo‘shiling! Biz EVOS taomlarini yetkazib berish uchun shaxsiy avtomobilga ega kuryerlar,"
"velokuryerlar va piyoda kuryerlarni izlayapmiz. Agar siz faol, punktual va moslashuvchan ish jadvalini izlayotgan bo‘lsangiz — bu ish aynan siz uchun!"
"Biz nimani taklif qilamiz"
"💰 Har haftada to‘lov"
"🕒 Moslashuvchan ish jadvali"
"EVOS’da har bir kuryer - jamoaning muhim a’zosi! @evos_jbot Telegram-botimizda anketani to‘ldiring va hoziroq EVOS bilan karyerangizni boshlang! 💼", photo=img)

@router.message(F.text == "Kantaktlar/Manzil")
async def kantakt_manzil(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_5.png"))
    await message.answer_photo(caption = "Toshkent sh., 100066, Chilonzor tumani,"
                                         " Furqat boshi berk ko'chasi, 175-uy. Ish vaqti: 9:00 - 18:00, Dam olish kunlari: shanba,"
                                         " yakshanba.", photo=img)

@router.message(F.text == "Yangiliklar")
async def yangiliklar(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_3.png"))
    await message.answer_photo(caption = "7:00 dan 10:00 gacha, kunni samarali boshlash uchun,"
                                         " ajoyib taomlarni topadigan maxsus menyudan bahramand bo’ling😊", photo=img)