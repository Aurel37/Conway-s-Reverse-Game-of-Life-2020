#modul to import data
import numpy as np
import pandas as pd


def open_csv(path, cols):
    data = pd.read_csv(path)
    return data[data.columns.difference(cols)]

def convertToNumpy(data):
    col_start = ['start_' + str(i) for i in range(625)]
    col_stop = ['stop_' + str(i) for i in range(625)]
    return (data[col_start].to_numpy().T, data[col_stop].to_numpy().T)

def convertArray(array, n=25, m=25):
    res = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            res[j][i] = array[i+n*j] #[j][i] and not [i][j]
    return res

def dataLoad(path, cols, n=25, m=25):
    """handle the opening of csv, and convertion of data into matrix
        @return : a tuple with the starts array and the stop arrays
        with size (for instance) (arrays(50,000, 25, 25), arrays(50,000, 25, 25))
        @param path : path of the csv
        @param cols : that does not represents the arrays
        @param n, m : size of the matrix (i.e. 25, 25)
    """
    data = open_csv(path, cols)
    arrays = convertToNumpy(data)
    p = arrays[0].shape[0]
    q = arrays[1].shape[0]
    resStart = np.zeros((p, n, m))
    resStop = np.zeros((q, n, m))
    for i in range(p):
        resStart[i] = convertArray(arrays[0][i], n, m)
    for i in range(p):
        resStop[i] = convertArray(arrays[1][i], n, m)
    return (resStart, resStop)