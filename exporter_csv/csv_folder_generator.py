import os
from datetime import datetime


def create_csv_folder(
        parent_folder_path: str):

    today_time = \
        datetime.today()


    folder_name = \
        f'{today_time.strftime("%b%d%Y%H%M%S")}\\'

    csv_folder_path = \
        os.path.join(
            parent_folder_path,
            folder_name)

    try:
        os.mkdir(
            csv_folder_path)

    except FileExistsError:
        print(
            'Target csv folder already exists.')

    return \
        csv_folder_path
