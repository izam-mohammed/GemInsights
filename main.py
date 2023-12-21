from gemInsights import logger
from gemInsights.pipeline.stage_00_data_ingestion import DataIngestionPredictionPipeline
from gemInsights.pipeline.stage_01_data_visualization import DataVisualizationPredictionPipeline
from gemInsights.pipeline.stage_02_prompt_generation import PromptGenerationPredictionPipeline
from gemInsights.pipeline.stage_03_prompting import PromptingPredictionPipeline

def run_pipeline(stage_name, pipeline_instance):
    """
    Run a specific stage of the sentiment analysis pipeline.

    Parameters:
    - stage_name: str
        Name of the pipeline stage.
    - pipeline_instance: object
        Instance of the pipeline stage to be executed.

    Returns:
        None
    """
    try:
        logger.info(f">>>>>> Stage {stage_name} started <<<<<<")
        pipeline_instance.main()
        logger.info(f">>>>>> Stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


if __name__ == "__main__":
    run_pipeline("Data Ingestion", DataIngestionPredictionPipeline())
    run_pipeline("data visualization", DataVisualizationPredictionPipeline())
    