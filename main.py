import os
import dotenv
import logging
from dotenv import load_dotenv
from aiohttp import web
from aioalice import Dispatcher, get_new_configured_app

#Setting logging

#initializing environment variables
dotenv_path = os.path.join(os.path.dirname(__file__,), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

WEBHOOK_URL_PATH = os.getenv('WEBHOOK_URL_PATH')
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')

#Setting basic dispatcher
dp = Dispatcher()
@dp.request_handler()
async def handle_all_requests(alice_request):
    return alice.request.response('Hello world!')
if __name__ == '__main__':
    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_URL_PATH)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)