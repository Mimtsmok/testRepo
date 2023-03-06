import asyncio
import logging

from flask import Flask

from bot import main

app = Flask(__name__)
loop = asyncio.get_event_loop()

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
