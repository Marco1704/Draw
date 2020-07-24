import pandas as pd
import pyodbc


def import_access_table(
        access_database_full_path: str) :

    driver = \
        r'{Microsoft Access Driver (*.mdb, *.accdb)}'

    connection_string = \
        r'Driver={};DBQ={}'.format(
            driver,
            access_database_full_path)

    connection = \
        pyodbc.connect(
            connection_string)
    query = \
        "SELECT * FROM 2004_2020_draw_results"

    tables_dataframe = \
        pd.read_sql_query(
            query,
            connection)

    '''table_name_list = \
        tables_dataframe['name'].tolist ()


    select_template = \
        'SELECT * FROM {table_name}'
    tables_frames_dict = \
        {}

    for tablename in table_name_list:
        query = \
            select_template.format(
                table_name=tablename)
        tables_frames_dict[tablename] = \
            pd.read_sql(
                query, connection )'''

    return \
        tables_dataframe