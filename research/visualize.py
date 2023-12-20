from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
import pandas as pd

filename = pd.read_csv("data/Iris.csv")
target_variable = "Species"

def get_ipython():
    def magic(hai):
        pass

dft = AV.AutoViz(
    "",
    sep=",",
    dfte=filename,
    depVar=target_variable,
    verbose=2,
    lowess=True,
    chart_format="svg",
    max_rows_analyzed=150000, 
    max_cols_analyzed=30,
)