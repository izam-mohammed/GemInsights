import os
from gemInsights import logger
import pandas as pd

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

    def store_data(self):
        """
        code for store the data into the cloud
        """