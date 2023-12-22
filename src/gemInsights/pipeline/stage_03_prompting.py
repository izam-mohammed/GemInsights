from gemInsights.config.configuration import ConfigurationManager
from gemInsights.components.prompting import Prompting
from gemInsights import logger


STAGE_NAME = "Data Prompt Generation stage"


class PromptingPredictionPipeline:
    def __init__(self):
        """
        Initialize Pipeline instance.
        """
        pass

    def main(self) -> None:
        """
        Execute the main steps of the pipeline.

        Returns:
            list: The prompt object as a list
        """
        config = ConfigurationManager()
        prompting_config = config.get_promting_config()
        prompting = Prompting(config=prompting_config)
        prompting.get_response()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PromptingPredictionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
