import pandas as pd
from gemInsights.utils.common import load_json, save_bin, save_txt
import os
import base64
from gemInsights import logger
from vertexai.preview.generative_models import Part
from pathlib import Path
from gemInsights.entity.config_entity import PromptGenerationConfig


class PromptGeneration:
    def __init__(self, config: PromptGenerationConfig):
        """
        Initialize the PromptGeneration object.

        Parameters:
        - config (PromptGenerationConfig): Configuration object for prompt generation.
        """
        self.config = config

    def generate(self) -> None:
        """
        Generate a prompt based on the provided configuration and dataset information.

        Reads a CSV file specified in the configuration, loads the dataset into a pandas DataFrame,
        loads additional information from a JSON file, loads images from a specified directory,
        generates a prompt string, and saves images and the prompt to binary files.

        Returns:
        None
        """
        df = pd.read_csv(self.config.data_path)
        info_json = load_json(Path(self.config.data_information_file))
        target_col = info_json.target_col
        additional_info = info_json.additional_info
        # df_shape = df.shape
        # df_columns = list(df.columns)
        # df_describe = str(df.describe())+"\n"+ str(df.describe(include=["O"]))

        images = []
        image_dir = os.path.join(self.config.visualization_path, target_col)
        image_files = os.listdir(image_dir)
        for image_file in image_files:
            image_path = os.path.join(image_dir, image_file)
            img = open(image_path, "rb").read()
            img_bytes = Part.from_data(
                base64.b64decode(base64.encodebytes(img)), mime_type="image/jpeg"
            )
            logger.info(f"added the image - {image_file}")
            images.append(img_bytes)

        prompt = f"{self.config.main_prompt}\n Here are some of the informations related to the dataset - '{additional_info}'"
        # f"This is the target column of the dataset - '{target_col}'",
        # f"The shape of the dataset is {df_shape}",
        # f"The columns in the dataset are {df_columns}",
        # f"Here are some of the general statistics related the dataset - {df_describe}",

        save_bin(
            data=images,
            path=Path(os.path.join(self.config.root_dir, self.config.images_file_name)),
        )
        save_txt(
            data=prompt,
            path=Path(os.path.join(self.config.root_dir, self.config.prompt_file_name)),
        )
