from gemInsights.constants import *
from gemInsights.utils.common import read_yaml, create_directories
from gemInsights.entity.config_entity import DataIngestionConfig

#udpate configuration manager
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        key_filepath = KEY_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.key = read_yaml(key_filepath)

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