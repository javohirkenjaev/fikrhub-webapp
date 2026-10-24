import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage

# Tokeningiz va veb sahifa ssilkasi
BOT_TOKEN = "888177697:AAHezQZ4pJQS1jJ5W3MSNxHi3-0MeZs1o6Y"
WEBAPP_URL = "https://javohirkenjayev.github.io/fikrhub-webapp/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
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

async def main():
    print("Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())