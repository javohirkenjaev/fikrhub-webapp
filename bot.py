import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage

# Tokeningizni va GitHub Pages ssilkatingizni shu yerga yozasiz
BOT_TOKEN = "8881776997:AAHezQZ4pJQSljJ5W3MSNxHi3-0MeZs1o6Y"
WEBAPP_URL = "https://javohirkenjayev.github.io/fikrhub-webapp/"

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# /start komandasi uchun handler
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # WebApp tugmasini yaratish
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📊 Biznes Analitikani Ko'rish",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )
    
    await message.answer(
        f"Assalomu alaykum, <b>{message.from_user.first_name}</b>! 👋\n\n"
        "<b>FikrHub</b> botiga xush kelibsiz. Quyidagi tugma orqali biznes analitika va boshqaruv paneliga o'tishingiz mumkin:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

# Botni ishga tushirish funksiyasi
async def main():
    print("Bot muvaffaqiyatli ishga tushdi! Telegramda /start ni bosing...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())