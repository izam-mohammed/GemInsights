from google.cloud import aiplatform
from gemInsights import logger
import os
import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
from gemInsights.utils.common import load_json, save_json
from gemInsights.entity.config_entity import PromptingConfig

class Prompting:
    def __init__(self, config: PromptingConfig):
        self.config = config

    def get_response(self):
        aiplatform.init(
            project = self.config.project_name,
            location= self.config.project_location,
        )
        logger.info(f"Google cloud project name - {self.config.project_name}")
        
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.config.credentials
        logger.info("loaded the google cloud credentials")

        model = GenerativeModel(self.config.model_name)
        logger.info(f"using the model - {self.config.model_name}")

        logger.info(f"generating response with config - {self.config.generation_config}")
        responses = model.generate_content(
            self.config.prompt,
            generation_config=self.config.generation_config,
            )
        
        save_json(path=os.path.join(self.config.root_dir, self.config.response_file_name), data={"response": responses.text})
        logger.info(responses.text)