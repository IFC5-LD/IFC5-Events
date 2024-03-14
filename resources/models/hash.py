from hashlib import sha256

def _hash_string(string: str) -> str:
    return sha256(string.encode('utf-8')).hexdigest()

def _hash_dict(dictionary: dict) -> str:
    return sha256(str(dictionary).encode('utf-8')).hexdigest()

def _hash_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()

def _hash_numeric(data: Union[int, float]) -> str:
    return sha256(str(data).encode('utf-8')).hexdigest()

def hash(data: Union[str, dict, int, float, bytes], encoding: str = 'utf-8') -> str:
    if isinstance(data, str):
        return _hash_string(data)
    elif isinstance(data, dict):
        return _hash_dict(data)
    elif isinstance(data, bytes):
        return _hash_bytes(data)
    elif isinstance(data, (int, float)):
        return _hash_numeric(data)
    else:
        raise ValueError("Data type not supported")