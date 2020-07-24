from import_access.access_importer import import_access_table
from table_analysis.number_counter_test import result_number_counter

draw_database_full_path = \
    'C:\\Users\\dasilvam\\OneDrive\\Python projects\\Draw\\database\\draw_numbers_V0.01.accdb'

#Importing draw table

draw_results_dataframe = import_access_table(draw_database_full_path)

print(draw_results_dataframe)
#Analysing the table

#number of times that a number appears in a row

number_counts_dataframe = result_number_counter( draw_results_dataframe)



print(number_counts_dataframe)

#print(number_counts_dict)
#print('d')

#number of times that a number appears in a column




#number of times that a number appears on the table