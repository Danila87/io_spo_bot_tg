from dataclasses import dataclass
from typing import Dict, Optional

from aiogram_dialog.api.entities import MediaAttachment


@dataclass
class DTOWithFile:
    file_path: Optional[str] = None
    file: Optional[MediaAttachment] = None
    data: Optional[Dict] = None