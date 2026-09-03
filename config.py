# import hvac
# import os
#
# from dotenv import load_dotenv
# from hvac.exceptions import InvalidPath
#
# load_dotenv()
#
# client = hvac.Client(
#     url=os.environ.get("VAULT_URL"),
#     token=os.environ.get('VAULT_TOKEN'),
# )
#
# try:
#     token = client.secrets.kv.v2.read_secret_version(
#         path="Bot_token", # Имя секрета
#         mount_point='pipif' # Имя engine
#     )
#     BOT_TOKEN = token['data']['data']['token']
# except InvalidPath:
#     print('Не найден токен для бота')
#
# try:
#     redis_data = client.secrets.kv.v2.read_secret_version(
#         path="Redis", # Имя секрета
#         mount_point='pipif' # Имя engine
#     )
#     REDIS_HOST = redis_data['data']['data']['host']
#     REDIS_PORT = int(redis_data['data']['data']['port'])
#     REDIS_PASSWORD = redis_data['data']['data']['password']
# except InvalidPath:
#     print('Не найдены параметры для redis')
#
# try:
#     api_data = client.secrets.kv.v2.read_secret_version(
#         path="Api", # Имя секрета
#         mount_point='pipif' # Имя engine
#     )
#     API_HOST = api_data['data']['data']['host']
#     API_PORT = int(api_data['data']['data']['port'])
# except InvalidPath:
#     print('Не найдены параметры для api')

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_PASSWORD = os.environ.get('REDIS_PASS')

API_HOST = os.environ.get('API_HOST')
API_PORT = os.environ.get('API_PORT')
