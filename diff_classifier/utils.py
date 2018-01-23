import pandas as pd
import numpy as np
import skimage.io as sio


def csv_to_pd(csvfname):
    csvfile = open(csvfname)

    line = 'test'
    counter = 0
    while line != 'Data starts here.\n':
        line = csvfile.readline()
        counter = counter + 1

    data = pd.read_csv(csvfname, skiprows=counter)
    data.sort_values(['Track_ID', 'Frame'], ascending=[1, 1])

    return data