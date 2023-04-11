import asyncio
import logging
import sys
from threading import Thread

from flask import Flask

from bot import main

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello():
    return "Hello"


class FlaskThread(Thread):
    def run(self) -> None:
        app.run(host="0.0.0.0", port=80)


class TelegramThread(Thread):
    async def run(self) -> None:
        await main()


if __name__ == "__main__":
    flask_thread = FlaskThread()
    flask_thread.start()

    main()
