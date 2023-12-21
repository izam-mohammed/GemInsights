from gemInsights.constants import *
from gemInsights.utils.common import read_yaml, create_directories
from gemInsights.entity.config_entity import (DataIngestionConfig,
                                              DataVisualizationConfig,
                                              PromptGenerationConfig,
                                              PromptingConfig)

#udpate configuration manager
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        credentials_file_path = CREDENTIALS_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.credentials = credentials_file_path
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
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
        config = self.config.data_visualization
        
        create_directories([config.root_dir])

        data_visualization_config = DataVisualizationConfig(
            root_dir=config.root_dir,
            data_file_path=config.data_file_path,
            info_file_path=config.info_file_path,
        )

        return data_visualization_config
    
    def get_prompt_generation_config(self) -> PromptGenerationConfig:
        config = self.config.prompt_generation
        
        create_directories([config.root_dir])

        prompt_generation_config = PromptGenerationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            visualization_path=config.visualization_path,
            data_information_file=config.data_information_file,
            prompt_file_name=config.prompt_file_name,
        )

        return prompt_generation_config
    

    def get_promting_config(self) -> PromptingConfig:
        config = self.config.prompting
        
        create_directories([config.root_dir])

        prompting_config = PromptingConfig(
            root_dir=config.root_dir,
            model_name=config.model_name, 
            response_file_name=config.response_file_name,
            candidates_file_name=config.candidates_file_name,
            credentials=self.credentials,
            generation_config=dict(self.params.generation_config),
            project_name=config.project_name,
            project_location=config.project_location,
            prompt_file_path=config.prompt_file_path,          
        )

        return prompting_config