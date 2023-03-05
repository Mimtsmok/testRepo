import asyncio
import logging

from flask import Flask

from bot import main

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/')
def hello():
    asyncio.run(main())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
