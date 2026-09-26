# Simple Aiogram Echo Bot

This is a minimal Telegram bot built with aiogram that echoes incoming messages.

## Setup

1. Create a virtual environment if needed.
2. Install dependencies:
   - `python3 -m pip install -r requirements.txt`
3. Set your Telegram bot token:
   - `export BOT_TOKEN="YOUR_TOKEN_HERE"`
   - or copy `.env.example` to `.env` and load it with your preferred method.
4. Run the bot:
   - `python3 bot.py`

## Commands

- `/start` — shows a welcome message
- Any text message — echoed back

## Notes

This bot is intentionally simple and meant as a starting point for larger aiogram projects.
