from gemInsights.config.configuration import ConfigurationManager
from gemInsights.components.prompt_generation import PromptGeneration
from gemInsights import logger


STAGE_NAME = "Data Prompt Generation stage"


class PromptGenerationPredictionPipeline:
    def __init__(self):
        """
        Initialize Pipeline instance.
        """
        pass

    def main(self):
        """
        Execute the main steps of the pipeline.

        Returns:
            list: The prompt object as a list
        """
        config = ConfigurationManager()
        prompt_generation_config = config.get_prompt_generation_config()
        prompt_generation = PromptGeneration(config=prompt_generation_config)
        prompt = prompt_generation.generate()
        return prompt


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PromptGenerationPredictionPipeline()
        logger.info(obj.main())
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
