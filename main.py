import asyncio
import logging
import sys

from flask import Flask

from bot import main

app = Flask(__name__)
if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    return "Hello"

@app.route('/start')
async def start():
    await main()
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
