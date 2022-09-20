from aiogram import Bot, Dispatcher, executor, types
from tg_bot.handlers import register_handlers


token = 'TOKEN'
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот онлайн!')

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
