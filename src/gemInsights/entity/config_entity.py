from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_data_file: Path
    source_info_file: Path
    local_data_name: str


@dataclass(frozen=True)
class DataVisualizationConfig:
    root_dir: Path
    data_file_path: Path
    info_file_path: Path


@dataclass(frozen=True)
class PromptGenerationConfig:
    root_dir: Path
    data_path: Path
    visualization_path: Path
    data_information_file: Path
    prompt_file_name: str
    images_file_name: str
    main_prompt: str


@dataclass(frozen=True)
class PromptingConfig:
    root_dir: Path
    model_name: str
    response_file_name: str
    candidates_file_name: str
    credentials: Path
    generation_config: dict
    project_name: str
    project_location: str
    prompt_file_path: Path
    images_file_path: Path