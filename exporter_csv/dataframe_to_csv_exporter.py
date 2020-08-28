def export_dataframe_to_csv(
        dataframe,
        csv_folder_path: str):
    dataframe.to_csv(fr'{csv_folder_path}\number_count.csv',index=None,header=True)
