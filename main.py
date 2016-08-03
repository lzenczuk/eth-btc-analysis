import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import mean, std
import numpy as np

from coindesk import load_coindesk_eur_prices
from iconomi import load_iconomi_eur_prices


def normalize_by_std(data_dict):
    d_mean = mean(data_dict.values())
    d_std = std(data_dict.values())

    for d in data_dict.keys():
        p = data_dict[d]
        data_dict[d] = (p - d_mean) / d_std

    return data_dict


def sub_set(data_dict, index, num):
    result_dict = {}

    keys = sorted(data_dict.keys())
    counter = 0

    for key in keys:
        if key >= index:
            result_dict.update({key: data_dict[key]})
            counter += 1
            if counter >= num:
                break

    return result_dict


def pair_prices(data_dict1, data_dict2):
    x_data = []
    y_data = []
    keys = data_dict1.keys()

    for key in keys:
        if key in data_dict2:
            x_data.append(data_dict1[key])
            y_data.append(data_dict2[key])

    return x_data, y_data


def pair_prices_with_offset(data_dict1, data_dict2, n):
    x_data = []
    y_data = []
    keys = data_dict1.keys()

    offset = n * 300

    for key in keys:
        if key + offset in data_dict2:
            x_data.append(data_dict1[key])
            y_data.append(data_dict2[key + offset])

    return x_data, y_data

def triangulate_prices(data_dict1, data_dict2):
    x_data = []
    y_data = []
    z_data = []

    keys = data_dict1.keys()

    for key in keys:
        if key in data_dict2:
            x_data.append(data_dict1[key])
            y_data.append(data_dict2[key])
            z_data.append(np.float32(key))

    return x_data, y_data, z_data


def plot_price_in_time(*data_dicts):
    for data_dict in data_dicts:
        x_dates = sorted(data_dict.keys())
        y_prices = []

        for date in x_dates:
            y_prices.append(data_dict[date])

        plt.plot(x_dates, y_prices)


coindesk_eur_prices = load_coindesk_eur_prices('data/coindesk_prices.csv')
iconomi_eur_prices = load_iconomi_eur_prices('data/iconomi_prices.csv')

#coindesk_data_dict = normalize_by_std(sub_set(coindesk_eur_prices, date_to_unix_long(2016, 7, 11), 288))
coindesk_data_dict = normalize_by_std(coindesk_eur_prices)
#iconomi_data_dict = normalize_by_std(sub_set(iconomi_eur_prices, date_to_unix_long(2016, 7, 11), 288))
iconomi_data_dict = normalize_by_std(iconomi_eur_prices)

#coindesk_iconomi_data = pair_prices_with_offset(coindesk_data_dict, iconomi_data_dict, 1)
#coindesk_iconomi_data = pair_prices_with_offset(coindesk_data_dict, iconomi_data_dict, 12)
coindesk_iconomi_data = triangulate_prices(coindesk_data_dict, iconomi_data_dict)

# plot_price_in_time(coindesk_data_dict, iconomi_data_dict)
#plt.plot(coindesk_iconomi_data[0], coindesk_iconomi_data[1], 'o')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(coindesk_iconomi_data[0], coindesk_iconomi_data[1], coindesk_iconomi_data[2])
plt.show()
#plt.savefig('iconomi.png')

#for q in range(0, 500, 100):
#    coindesk_iconomi_data = pair_prices_with_offset(coindesk_data_dict, iconomi_data_dict, q)
#    plt.plot(coindesk_iconomi_data[0], coindesk_iconomi_data[1], 'o')
#    plt.savefig('iconomi' + str(q) + '.png')
