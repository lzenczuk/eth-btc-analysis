import csv
import numpy as np
from util import java_date_to_unix_long_rounded_to_minutes


def load_coindesk_eur_prices(csv_data_file_path):
    coindesk_data_dict = {}

    with open(csv_data_file_path, 'r') as coindesk_csv:
        coindesk_csv_reader = csv.reader(coindesk_csv)
        for row in coindesk_csv_reader:
            coindesk_data_dict.update({java_date_to_unix_long_rounded_to_minutes(row[0]): np.float32(row[2])})

    return coindesk_data_dict
