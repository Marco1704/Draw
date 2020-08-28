import pandas as pd
from collections import Counter


def result_number_counter_test(
        dataframe:pd.DataFrame):

    cstn = Counter (dataframe)
    cstlist = pd.DataFrame.from_dict (cstn, orient='index' ).reset_index ()
    cstlist.columns = ['name', 'cnt']
    dataframe['cnt'] = dataframe['cst'].map(cstlist.loc[:, ['name', 'cnt']].set_index ('name').iloc[:, 0].to_dict () )
