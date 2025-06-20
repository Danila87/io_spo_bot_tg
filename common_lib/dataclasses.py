from dataclasses import dataclass

@dataclass
class FileData:
    filename: str
    data: bytes
    file_type: str