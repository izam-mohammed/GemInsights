import os
from box.exceptions import BoxValueError
import yaml
from gemInsights import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import numpy as np

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def save_bin_dup(data, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    ls = sorted(os.listdir(os.path.dirname(path)))
    number = os.path.splitext(ls[-1])[0][-2:]
    if number == "__":
        num_int = 1
    else:
        num_int = int(number) + 1
    str_num = str(num_int).zfill(2)
    name, ext = os.path.splitext(path)
    file_name = f"{name}_{str_num}{ext}"
    joblib.dump(value=data, filename=file_name)

    logger.info(f"binary file saved at: {file_name}")


@ensure_annotations
def load_bin(path: Path):
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def save_txt(data, path: Path):
    """save text file

    Args:
        data (Any): data to be saved as text
        path (Path): path to text file
    """
    with open(path, "w") as f:
        f.write(data)

    logger.info(f"txt file saved at: {path}")

def is_nan(value):
    """Check if a value is NaN.

    Args:
        values (Any): Any values

    Returns:
        Bool: type of the value is na
    """
    return isinstance(value, float) and np.isnan(value)

def round_batch(*vars):
    """
    Round a batch of values individually

    Args:
        Any

    Returns:
        tuple: contain all values in batch
    """
    res = []
    for i in vars:
        res.append(round(i, 3))
    return tuple(res)

