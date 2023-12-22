from gemInsights.utils.common import load_json
from autoviz import AutoViz_Class
from gemInsights import logger
from gemInsights.entity.config_entity import DataVisualizationConfig
from pathlib import Path
import os


class DataVisualization:
    def __init__(self, config: DataVisualizationConfig):
        """
        Initialize the DataVisualization object.

        Parameters:
        - config (DataVisualizationConfig): Configuration object for data visualization.
        """
        self.config = config

    def visualize(self) -> None:
        """
        Generate visualizations for the specified data file and save the plots.

        Uses AutoViz to automatically generate visualizations for the specified data file.
        The generated plots are saved in the directory specified in the configuration.

        Returns:
        None
        """
        data_info = load_json(Path(self.config.info_file_path))
        target_col = data_info.target_col

        AV = AutoViz_Class()

        dft = AV.AutoViz(
            "",
            sep=",",
            depVar=target_col,
            dfte=self.config.data_file_path,
            header=0,
            verbose=2,
            lowess=False,
            chart_format="jpg",
            max_rows_analyzed=500,
            max_cols_analyzed=20,
            save_plot_dir=self.config.root_dir,
        )

        logger.info(f"saved the plots")
