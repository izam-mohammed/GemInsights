from gemInsights.config.configuration import ConfigurationManager
from gemInsights.components.data_ingestion import DataIngestion
from gemInsights import logger


STAGE_NAME = "Data Ingestion stage"


class DataIngestionPredictionPipeline:
    def __init__(self):
        """
        Initialize DataIngestionTrainingPipeline instance.
        """
        pass

    def main(self):
        """
        Execute the main steps of the data ingestion training pipeline.

        Returns:
            None
        """
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.load_data()
        data_ingestion.load_info()
        data_ingestion.store_data()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPredictionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e