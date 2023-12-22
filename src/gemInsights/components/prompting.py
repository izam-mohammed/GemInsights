from google.cloud import aiplatform
from gemInsights import logger
import os
import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
from gemInsights.utils.common import load_json, save_json, load_bin, read_text
from trulens_eval import Feedback, Tru, LiteLLM, Huggingface, TruBasicApp
from trulens_eval.feedback import Groundedness
from gemInsights.entity.config_entity import PromptingConfig
from pathlib import Path


class Prompting:
    def __init__(self, config: PromptingConfig):
        """
        Initialize the Prompting object.

        Parameters:
        - config (PromptingConfig): Configuration object for prompting.
        """
        self.config = config

    def _setup_env(self) -> None:
        """
        Set up the environment for Trulens and Google Cloud.

        Initialize Trulens and set up Google Cloud credentials.

        Returns:
        None
        """
        tru = Tru()
        # tru.reset_database()
        logger.info(f"initialized trulens with db")

        aiplatform.init(
            project=self.config.project_name,
            location=self.config.project_location,
        )
        logger.info(f"Google cloud project name - {self.config.project_name}")

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.config.credentials
        logger.info("loaded the google cloud credentials")

        self.model = GenerativeModel(self.config.model_name)
        logger.info(f"using the model - {self.config.model_name}")

    def _set_feedback(self) -> None:
        """
        Set up feedback functions for evaluation.

        Uses LiteLLM for feedback on various aspects like criminality, insensitivity, etc.

        Returns:
        None
        """
        provider = LiteLLM(
            model_engine="chat-bison-32k", max_output_tokens=2048, temperature=0.0
        )
        grounded = Groundedness(groundedness_provider=provider)

        # LLM-based feedback functions
        f_criminality = Feedback(
            provider.criminality_with_cot_reasons,
            name="Criminality",
            higher_is_better=False,
        ).on_output()

        f_insensitivity = Feedback(
            provider.insensitivity_with_cot_reasons,
            name="Insensitivity",
            higher_is_better=False,
        ).on_output()

        f_maliciousness = Feedback(
            provider.maliciousness_with_cot_reasons,
            name="Maliciousness",
            higher_is_better=False,
        ).on_output()

        f_hate = Feedback(
            provider.harmfulness_with_cot_reasons,
            name="Harmfulness",
            higher_is_better=False,
        ).on_output()

        f_controvertial = Feedback(
            provider.controversiality_with_cot_reasons,
            name="Coherence",
            higher_is_better=False,
        ).on_output()

        f_coherence = Feedback(
            provider.coherence_with_cot_reasons,
            name="Coherence",
            higher_is_better=True,
        ).on_output()

        f_currectness = Feedback(
            provider.correctness_with_cot_reasons,
            name="Currectness",
            higher_is_better=True,
        ).on_output()

        f_helpful = Feedback(
            provider.helpfulness_with_cot_reasons,
            name="Helpfulness",
            higher_is_better=True,
        ).on_output()

        f_conciseness = Feedback(
            provider.conciseness_with_cot_reasons,
            name="Conciseness",
            higher_is_better=True,
        ).on_output()

        self.all_feedbacks = [
            f_coherence,
            f_currectness,
            f_helpful,
            f_conciseness,
            f_criminality,
            f_insensitivity,
            f_maliciousness,
            f_hate,
            f_controvertial,
        ]

        logger.info("loaded all feedback functions")

    def _initiate_data(self) -> None:
        """
        Load prompt and images data.

        Reads prompt text and images from specified files.

        Returns:
        None
        """
        self.prompt = read_text(Path(self.config.prompt_file_path))
        self.images = load_bin(Path(self.config.images_file_path))
        logger.info("initialized the prompt and the image file")

    def get_response(self) -> None:
        """
        Generate a response using the configured model and feedback functions.

        Sets up the environment, loads data, and uses the configured model to generate a response.
        The generated response is saved to a JSON file.

        Returns:
        None
        """
        self._setup_env()
        self._initiate_data()
        self._set_feedback()

        model = self.model
        images = self.images
        logger.info(type(self.images))
        configuration = self.config.generation_config

        def _llm_standalone(prompt):
            return model.generate_content(
                [prompt] + images, generation_config=configuration
            ).text

        tru_app_recorder = TruBasicApp(
            _llm_standalone, app_id="Sentiment bot", feedbacks=self.all_feedbacks
        )
        logger.info("created the basic recorder app")

        logger.info(
            f"generating response with config - {self.config.generation_config}"
        )
        with tru_app_recorder as records:
            response = tru_app_recorder.app("generate something")

        save_json(
            path=os.path.join(self.config.root_dir, self.config.response_file_name),
            data={"response": response},
        )
        logger.info(response)
