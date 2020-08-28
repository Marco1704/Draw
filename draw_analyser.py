from exporter_csv.csv_folder_generator import create_csv_folder
from exporter_csv.dataframe_to_csv_exporter import export_dataframe_to_csv
from import_access.access_importer import import_access_table
from results_analyser import result_analysis
from table_analysis.number_counter import result_number_counter, row_value_counter

csv_parent_folder_path = 'C:\\Users\\dasilvam\\OneDrive\\Python projects\\Draw\\csv_exporter'

#exceL_file_full_path = 'C:\Users\dasilvam\OneDrive\Python projects\Draw\euromillions results.xlsx'

draw_database_full_path = \
    'C:\\Users\\dasilvam\\OneDrive\\Python projects\\Draw\\database\\draw_numbers_V0.02.accdb'

# Importing draw table

draw_results_dataframe = import_access_table ( draw_database_full_path )

print ( draw_results_dataframe )

# number of times that a number appears in a column

number_counts_dataframe = result_number_counter ( draw_results_dataframe )

# count_result = result_number_counter_test(
# dataframe=draw_results_dataframe)

csv_folder_full_path = create_csv_folder ( parent_folder_path=csv_parent_folder_path )

# export_dataframe_to_csv(dataframe=count_result, csv_folder_path=csv_folder_full_path)

export_dataframe_to_csv ( dataframe=number_counts_dataframe, csv_folder_path=csv_folder_full_path )

print ( number_counts_dataframe )

# export_dataframe_to_access (dataframe=count_result, csv_folder_path=csv_folder_full_path)


# Analysing the table

row_counter = \
    row_value_counter (draw_results_dataframe)

results_mean = result_analysis(draw_results_dataframe)
print(results_mean)

print ( row_counter )

# number of times that a number appears on the table
