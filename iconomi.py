import csv
import numpy as np
from util import java_date_to_unix_long_rounded_to_minutes


def load_iconomi_eur_prices(csv_data_file_path):
    iconomi_data_dict = {}

    with open(csv_data_file_path, 'r') as iconomi_csv:
        iconomi_csv_reader = csv.reader(iconomi_csv)
        for row in iconomi_csv_reader:
            iconomi_data_dict.update({java_date_to_unix_long_rounded_to_minutes(row[0]): np.float32(row[1])})

    return iconomi_data_dict
