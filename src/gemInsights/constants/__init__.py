from pathlib import Path
from os import environ

CONFIG_FILE_PATH = Path("config/config.yaml")
KEY_FILE_PATH = Path("gemini_key.json")

if not KEY_FILE_PATH:
    raise KeyError("GEMINI_API_KEY not found !!!")