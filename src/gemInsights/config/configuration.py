from gemInsights.constants import *
from gemInsights.utils.common import read_yaml, create_directories, read_text, load_json
from pathlib import Path
from gemInsights.entity.config_entity import (
    DataIngestionConfig,
    DataVisualizationConfig,
    PromptGenerationConfig,
    PromptingConfig,
)


# udpate configuration manager
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        credentials_file_path=CREDENTIALS_FILE_PATH,
        params_file_path=PARAMS_FILE_PATH,
        prompt=MAIN_PROMPT_FILE_PATH,
    ):
        """
        Initialize the ConfigurationManager.

        Parameters:
        - config_filepath (str): Path to the configuration file.
        - credentials_file_path (str): Path to the Google Cloud credentials file.
        - params_file_path (str): Path to the parameters file.
        - prompt (str): Path to the main prompt file.
        """
        self.config = read_yaml(config_filepath)
        self.credentials = credentials_file_path
        self.params = read_yaml(params_file_path)
        self.prompt = read_text(prompt)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get the configuration for data ingestion.

        Returns:
        DataIngestionConfig: Configuration for data ingestion.
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_data_file=config.source_data_file,
            source_info_file=config.source_info_file,
            local_data_name=config.local_data_name,
        )

        return data_ingestion_config

    def get_data_visualization_config(self) -> DataVisualizationConfig:
        """
        Get the configuration for data visualization.

        Returns:
        DataVisualizationConfig: Configuration for data visualization.
        """
        config = self.config.data_visualization

        create_directories([config.root_dir])

        data_visualization_config = DataVisualizationConfig(
            root_dir=config.root_dir,
            data_file_path=config.data_file_path,
            info_file_path=config.info_file_path,
        )

        return data_visualization_config

    def get_prompt_generation_config(self) -> PromptGenerationConfig:
        """
        Get the configuration for prompt generation.

        Returns:
        PromptGenerationConfig: Configuration for prompt generation.
        """
        config = self.config.prompt_generation

        create_directories([config.root_dir])

        prompt_generation_config = PromptGenerationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            visualization_path=config.visualization_path,
            data_information_file=config.data_information_file,
            prompt_file_name=config.prompt_file_name,
            main_prompt=self.prompt,
            images_file_name=config.images_file_name,
        )

        return prompt_generation_config

    def get_promting_config(self) -> PromptingConfig:
        """
        Get the configuration for prompting.

        Returns:
        PromptingConfig: Configuration for prompting.
        """
        config = self.config.prompting

        create_directories([config.root_dir])

        prompting_config = PromptingConfig(
            root_dir=config.root_dir,
            model_name=config.model_name,
            response_file_name=config.response_file_name,
            candidates_file_name=config.candidates_file_name,
            credentials=self.credentials,
            generation_config=dict(self.params.generation_config),
            project_name=load_json(Path(self.credentials)).project_id,
            project_location=config.project_location,
            prompt_file_path=config.prompt_file_path,
            images_file_path=config.images_file_path,
        )

        return prompting_config
