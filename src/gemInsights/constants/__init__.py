from pathlib import Path
from os import environ

CONFIG_FILE_PATH = Path("config/config.yaml")
CREDENTIALS_FILE_PATH = "credentials/cloud_credentials.json"
PARAMS_FILE_PATH = Path("params.yaml")
MAIN_PROMPT_FILE_PATH = Path("prompts/main_prompt.txt")

if not Path(CREDENTIALS_FILE_PATH):
    raise KeyError(
        "cloud credentials not found !!! Add credentials as cloud_credentials.json in credentials folder"
    )
