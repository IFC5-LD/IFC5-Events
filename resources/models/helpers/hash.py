from hashlib import sha256
from typing import Union


def _hash_string(string: str, encoding: str = "utf-8") -> str:
    return sha256(string.encode(encoding)).hexdigest()


def _hash_dict(dictionary: dict, encoding: str = "utf-8") -> str:
    return sha256(str(dictionary).encode(encoding)).hexdigest()


def _hash_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


def _hash_numeric(data: Union[int, float], encoding: str = "utf-8") -> str:
    return sha256(str(data).encode('utf-8')).hexdigest()


def hash(data: Union[str, dict, int, float, bytes], encoding: str = 'utf-8') -> str:
    if isinstance(data, str):
        return _hash_string(data, encoding)
    elif isinstance(data, dict):
        return _hash_dict(data, encoding)
    elif isinstance(data, bytes):
        return _hash_bytes(data)
    elif isinstance(data, (int, float)):
        return _hash_numeric(data, encoding)
    else:
        raise ValueError("Data type not supported")
