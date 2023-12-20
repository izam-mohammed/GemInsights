from gemInsights.config.configuration import ConfigurationManager
from gemInsights.components.data_visualization import DataVisualization
from gemInsights import logger


STAGE_NAME = "Data Visualization stage"


class DataVisualizationPredictionPipeline:
    def __init__(self):
        """
        Initialize Pipeline instance.
        """
        pass

    def main(self):
        """
        Execute the main steps of the data visualize prediction pipeline.

        Returns:
            None
        """
        config = ConfigurationManager()
        data_visualizaton_config = config.get_data_visualization_config()
        data_visualizaton = DataVisualization(config=data_visualizaton_config)
        data_visualizaton.visualize()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataVisualizationPredictionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e