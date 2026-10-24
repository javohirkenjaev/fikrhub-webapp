
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage

# --- SOZLAMALAR ---
# O'zingizning to'g'ri manzillaringizni qo'ying
BOT_TOKEN = "888177697:AAHezQZ4pJQS1jJ5W3MSNxHi3-0MeZs1o6Y"
WEBAPP_URL = "https://javohirkenjaev.github.io/fikrhub-webapp/" 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

def get_webapp_keyboard():
    """Web App ni ochuvchi maxsus tugma"""
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 FikrHub Platformasini Ochish", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    return markup

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    """Botga start bosilganda ishlaydigan asosiy funksiya"""
    user_name = message.from_user.first_name
    welcome_text = (
        f"Assalomu alaykum, <b>{user_name}</b>! 🌟\n\n"
        f"<b>FikrHub</b> - eng yirik do'konlar va xizmatlar platformasiga xush kelibsiz.\n"
        f"Quyidagi tugmani bosib platformaga kiring, o'z do'koningizni yarating yoki tavsiyalarni ko'ring!"
    )
    await message.answer(welcome_text, reply_markup=get_webapp_keyboard(), parse_mode="HTML")

@dp.message(F.successful_payment)
async def process_successful_payment(message: types.Message):
    """Kelajakda to'lovlar (Telegram Stars / Click) ulanganida ishlaydi"""
    await message.answer("🎉 To'lovingiz muvaffaqiyatli qabul qilindi! VIP obunangiz faollashdi.")

async def main():
    try:
        print("🚀 FikrHub Boti mukammal holatda ishga tushdi!")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())