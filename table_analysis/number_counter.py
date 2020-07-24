

def result_number_counter(
        dict_of_dataframes):

    number_repetition_dict = dict_of_dataframes.value_counts ()

    return number_repetition
    #number_count_row = 0
    #number_count_column = 0

    '''number_repetition = {}
    for table, dataframe in dict_of_dataframes.items():
        for value in dataframe:
            value.count()
            number_count_row += 1

         for value in dataframe:
            value.count(axis='columns')
            number_count_column +=1'''
