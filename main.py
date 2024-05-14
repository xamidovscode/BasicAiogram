from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '6553483159:AAG-j_qQ0A1bvnfG9SbaevNHHx13S1DKsqQ'

bot = Bot(TOKEN_API)

dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text='ishlamoqda')


if __name__ == '__main__':
    executor.start_polling(dp)
