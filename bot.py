import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN not found. Create a .env file with BOT_TOKEN=your_token_here "
        "or export BOT_TOKEN in your shell before running the bot."
    )

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(
        "Hello! I am an echo bot. Send me any text and I will repeat it back."
    )


@dp.message()
async def echo_handler(message: Message) -> None:
    username = message.from_user.username if message.from_user and message.from_user.username else "Unknown"
    text = message.text or "[media]"

    print(f"[BOT STATUS] New message from @{username}: {text}")

    if message.text is not None:
        await message.answer(message.text)
    elif message.sticker is not None:
        await message.answer_sticker(message.sticker.file_id)
    else:
        await message.answer("I can echo text and stickers.")


async def main() -> None:
    print("[BOT STATUS] Bot is running and polling for messages...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
