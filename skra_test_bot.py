from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# There is a bot's name
BOT_TOKEN = '8135283680:AAFH31-AWM-3tLbQ0LaFQNZ4P-QEhDQ2j4E'

# Create a bot and dispatcher objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Create handler that will be work by use command /start
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши что-нибудь :)')


# Create handler that will be work by use command /help
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши че нить\n'
        'Отвечу :3'
    )


# Create handler that will work with any message beside '/start' and '/help'
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
            'метод send_copy'
        )

if __name__ == '__main__':
    dp.run_polling(bot)
