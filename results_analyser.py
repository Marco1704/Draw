import pandas as pd

def result_analysis(
        dataframe:pd.DataFrame):

    mean_results = dataframe.describe(include='all')

    return mean_results