import pandas as pd
from gemInsights.utils.common import load_json
import os
import PIL.Image
from gemInsights import logger
from gemInsights.entity.config_entity import PromptGenerationConfig
from pathlib import Path

class PromptGeneration:
    def __init__(self, config: PromptGenerationConfig):
        self.config = config

    def generate(self):
        df = pd.read_csv(self.config.data_path)
        info_json = load_json(Path(self.config.data_information_file))
        target_col = info_json.target_col
        additional_info = info_json.additional_info
        df_shape = df.shape
        df_columns = list(df.columns)
        df_describe = str(df.describe())+"\n"+ str(df.describe(include=["O"]))
        main_prompt = "Act as a data analyst. Here is the complete information and visualization images of a dataset. give valuable insights from the data point wise"
        images = []
        image_dir = os.path.join(self.config.visualization_path, target_col)
        image_files = os.listdir(image_dir)
        for image_file in image_files:
            image_path = os.path.join(image_dir, image_file)
            img = PIL.Image.open(image_path)
            images.append(img)

        prompt = [
            main_prompt,
            f"This is the target column of the dataset - '{target_col}'",
            f"Here are some of the informations related to the dataset - '{additional_info}'",
            f"The shape of the dataset is {df_shape}",
            f"The columns in the dataset are {df_columns}",
            f"Here are some of the general statistics related the dataset - {df_describe}",
        ]

        result = prompt +images
        return result