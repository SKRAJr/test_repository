import pprint
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram import F

# There is a bot's name
BOT_TOKEN = '8135283680:AAFH31-AWM-3tLbQ0LaFQNZ4P-QEhDQ2j4E'

# Create a bot and dispatcher objects
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Create handler that will be work by use command /start
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши что-нибудь :)')


# Create handler that will be work by use command /help
async def process_help_command(message: Message):
    await message.answer(
        'Напиши че нить\n'
        'Отвечу :3'
    )


# Create handler that will work with any message beside '/start' and '/help'
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Create handler that will work with photo_type message
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# Create handler that will work with sticker_type
async def send_sticker_echo(message: Message):
    pprint.pprint(message)
    await message.reply_sticker(message.sticker.file_id)


# Register our handlers
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
