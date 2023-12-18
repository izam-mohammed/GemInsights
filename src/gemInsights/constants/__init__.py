from pathlib import Path
from os import environ

CONFIG_FILE_PATH = Path("config/config.yaml")
GEMINI_API_KEY = environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise KeyError("GEMINI_API_KEY not found !!!")