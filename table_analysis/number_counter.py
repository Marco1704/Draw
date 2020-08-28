import pandas as pd


def result_number_counter (
        dataframe: pd.DataFrame) :
    count_list = []
    column_names = dataframe.columns.tolist ()

    final_count = pd.DataFrame ( [] )

    for name in column_names :
        count = dataframe[name].value_counts ()
        count_list.append ( count )

        final_count = final_count.append ( count_list )

        count_list.clear ()

    print ( final_count )
    return final_count


def row_value_counter (
        dataframe: pd.DataFrame) :

    duplicatedrowsdf = dataframe[dataframe.duplicated ()]

    return duplicatedrowsdf
