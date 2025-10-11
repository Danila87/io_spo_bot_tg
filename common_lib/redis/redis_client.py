import json
import logging
from dataclasses import asdict

import redis
from functools import wraps

from aiogram_dialog.api.entities import MediaAttachment

from common_lib.utils import get_file_content_type
from config import REDIS_PASSWORD, REDIS_PORT, REDIS_HOST
from pathlib import Path

from schemas.dto import DTOWithFile

redis = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    #password=REDIS_PASS
)

def cache_data_file(
        expire=600
):
    def decorator(
            func
    ):
        @wraps(func)
        async def wrapper(
                *args,
                **kwargs
        ):
            dialog_manager = kwargs.get('dialog_manager')
            data_data = dialog_manager.dialog_data
            redis_key = f"{func.__name__}&{''.join('?={}-{}'.format(key, value) for key, value in data_data.items())}"

            if data := redis.get(
                redis_key
            ):
                data = json.loads(data)

                file = Path(data['file_path'])
                content_type = get_file_content_type(file.suffix)
                file_media = MediaAttachment(type=content_type, path=str(file.resolve()))

                return {
                    'file_path': str(file.resolve()),
                    'file': file_media,
                    'data': data['data']
                }

            result: DTOWithFile = await func(*args, **kwargs)

            if not result.file_path:
                logging.error('Пустое значение пути к файлу. Кеширование невозможно')
                return asdict(result)

            cache_data = {
                'data': result.data,
                'file_path': result.file_path
            }

            redis.setex(
                name=redis_key,
                value=json.dumps(cache_data),
                time=expire
            )

            return asdict(result)
        return wrapper
    return decorator
