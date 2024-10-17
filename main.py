
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio


TOKEN = 'токен'


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в игру 'Кости'! Напишите /roll, чтобы бросить кости.")

@dp.message(Command("roll"))
async def roll_command(message: types.Message):
    import random
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total = dice_1 + dice_2
    await message.answer(f"Вы бросили кости:\n🎲 Кость 1: {dice_1}\n🎲 Кость 2: {dice_2}\n🎲 Общий результат: {total}")

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Используйте команды:\n/start - Начать игру\n/roll - Бросить кости\n/help - Справка")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
