from enum import Enum, auto
import os

class EnvKey(Enum):
    MONGO_URL = auto()

def get_env(key: EnvKey, default_value: str = None) -> str:
    return os.environ.get(key.name, default_value)