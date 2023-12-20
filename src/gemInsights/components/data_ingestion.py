import os
from gemInsights import logger
import pandas as pd
from gemInsights.utils.common import load_json, save_json
from gemInsights.entity.config_entity import DataIngestionConfig
from pathlib import Path

# components
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def load_data(self):
        data_path = Path(self.config.source_data_file)
        df = pd.read_csv(data_path)
        logger.info(f"loaded the dataframe with shape {df.shape}")

        df.to_csv(os.path.join(self.config.root_dir, self.config.local_data_name))
        logger.info(f"saved the data in {os.path.join(self.config.root_dir, self.config.local_data_name)}")

    def load_info(self):
        json_file = load_json(path=Path(self.config.source_info_file))
        data_name, _ = os.path.splitext(self.config.local_data_name)
        save_json(path=Path(os.path.join(self.config.root_dir, data_name+"_info.json")), data=json_file)

    def store_data(self):
        """
        code for store the data into the cloud
        """