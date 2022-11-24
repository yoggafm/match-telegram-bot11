import os

BOT_TOKEN = os.getenv('5728932780:AAFQ-Hz0QAQHIV7j7s8hiH0n6Fj9adfKfhQ')

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{5728932780:AAFQ-Hz0QAQHIV7j7s8hiH0n6Fj9adfKfhQ}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
