import h5py
import numpy as np

def get2dHistograms(path):
    f = h5py.File(path)
    keys = list(f.keys())
    dataset = [f[key]["data"] for key in keys]
    return dataset

def dataToArray(path):
    return np.array(get2dHistograms(path))