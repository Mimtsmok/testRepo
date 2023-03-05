from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from config_reader import config

# Bot token can be obtained via https://t.me/BotFahter
TOKEN = config.bot_token.get_secret_value()

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        # Send copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)
