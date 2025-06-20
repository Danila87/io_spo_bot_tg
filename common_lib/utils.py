from pathlib import Path

from aiogram.enums import ContentType
from aiogram_dialog.api.entities import MediaAttachment

from typing import Dict, Optional
from datetime import datetime

from common_lib.api_client.client import api_client
from .dataclasses import FileData

async def save_file(
        file_data: FileData
) -> Path:
    file = Path(Path(__file__).resolve().parents[1], 'temp', file_data.filename.replace('/', '|'))

    with file.open('wb') as f:
        f.write(file_data.data)

    return file.resolve()

def get_file_content_type(
        file_suffix: str
) -> ContentType:
    content_type = ContentType.DOCUMENT

    if file_suffix in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'):
        content_type = ContentType.PHOTO

    elif file_suffix in ('.mp3', '.wav', '.ogg', '.flac', '.m4a'):
        content_type = ContentType.AUDIO

    elif file_suffix in ('.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv'):
        content_type = ContentType.VIDEO

    elif file_suffix in ('.pdf', '.doc', '.docx', '.txt', '.rtf', '.xlsx', '.pptx'):
        content_type = ContentType.DOCUMENT

    return content_type

async def get_file(
        url: str,
        params: Dict
) -> Optional[MediaAttachment]:

    if (file_data := await api_client.get_file(
            url=url,
            params=params
        )) is None:
            return None

    else:
        if file_data.filename is None:
            file_data.filename = f'{datetime.now().isoformat()}{file_data.file_type}'

        if not (file := Path('temp', file_data.filename)).exists():
            file = await save_file(
                file_data=file_data
            )

    content_type = get_file_content_type(file.suffix)

    return MediaAttachment(
        type=content_type,
        path=str(file.resolve())
    )