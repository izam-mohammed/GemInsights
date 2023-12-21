from google.cloud import aiplatform
from gemInsights import logger
import os
import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
from gemInsights.utils.common import load_json, save_json, load_bin, read_text
from trulens_eval import Feedback, Tru, LiteLLM, Huggingface, TruBasicApp
from gemInsights.entity.config_entity import PromptingConfig
from pathlib import Path


class Prompting:
    def __init__(self, config: PromptingConfig):
        self.config = config

    def _setup_env(self):
        tru = Tru()
        # tru.reset_database()
        logger.info(f"initialized trulens with db")

        aiplatform.init(
            project = self.config.project_name,
            location= self.config.project_location,
        )
        logger.info(f"Google cloud project name - {self.config.project_name}")
        
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.config.credentials
        logger.info("loaded the google cloud credentials")

        self.model = GenerativeModel(self.config.model_name)
        logger.info(f"using the model - {self.config.model_name}")

        # first feedback function
        hugs = Huggingface()
        self.f_sentiment = Feedback(hugs.positive_sentiment).on_output()
        logger.info(f"initialized huggingface based sentiment feedback")

    def _initiate_data(self):
        print(f"{self.config.prompt_file_path}")
        self.prompt = read_text(Path(self.config.prompt_file_path))
        self.images = load_bin(Path(self.config.images_file_path))


    def get_response(self):
        self._setup_env()
        self._initiate_data()
        
        model = self.model
        images = self.images
        logger.info(type(self.images))
        configuration = self.config.generation_config

        def _llm_standalone(prompt):
            return model.generate_content(
                [prompt]+images , generation_config=configuration).text
        
        tru_app_recorder = TruBasicApp(_llm_standalone, app_id="Sentiment bot", feedbacks=[self.f_sentiment])
        logger.info("created the basic recorder app")

        logger.info(f"generating response with config - {self.config.generation_config}")
        with tru_app_recorder as records:
            response = tru_app_recorder.app("generate something")
        
        save_json(path=os.path.join(self.config.root_dir, self.config.response_file_name), data={"response": response})
        logger.info(response)