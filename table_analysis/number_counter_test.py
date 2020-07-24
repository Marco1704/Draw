import pandas as pd
from collections import Counter


def result_number_counter (
        dataframe: pd.DataFrame) :
    for column in dataframe :
        value_count = dataframe.groupby (column).size ().reset_index ( name='count' )

        print ( value_count )

    return value_count
# value_count = dataframe[column].value_counts()
