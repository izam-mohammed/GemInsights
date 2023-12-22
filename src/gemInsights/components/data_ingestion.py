import os
from gemInsights import logger
import pandas as pd
from gemInsights.utils.common import load_json, save_json
from gemInsights.entity.config_entity import DataIngestionConfig
from pathlib import Path


# components
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initialize the DataIngestion object.

        Parameters:
        - config (DataIngestionConfig): Configuration object for data ingestion.
        """
        self.config = config

    def load_data(self) -> None:
        """
        Load data from the source file, save it locally, and log the process.

        Reads a CSV file specified in the configuration, loads it into a pandas DataFrame,
        saves the DataFrame to a local CSV file, and logs the process.

        Returns:
        None
        """
        data_path = Path(self.config.source_data_file)
        df = pd.read_csv(data_path)
        logger.info(f"loaded the dataframe with shape {df.shape}")

        df.to_csv(os.path.join(self.config.root_dir, self.config.local_data_name))
        logger.info(
            f"saved the data in {os.path.join(self.config.root_dir, self.config.local_data_name)}"
        )

    def load_info(self) -> None:
        """
        Load information from a JSON file, modify the data name, save it locally, and log the process.

        Reads a JSON file specified in the configuration, extracts information, modifies the
        data name, saves the information to a local JSON file, and logs the process.

        Returns:
        None
        """
        json_file = load_json(path=Path(self.config.source_info_file))
        data_name, _ = os.path.splitext(self.config.local_data_name)
        save_json(
            path=Path(os.path.join(self.config.root_dir, data_name + "_info.json")),
            data=json_file,
        )
