import numpy as np
from gensim import corpora
from itertools import islice
import pickle as pkl


int_v = 50000

with open('./data/corpus_{}.mm'.format(1), 'rb') as f:
    data = pkl.load(f)
print(len(data))
print(type(data))


def static_single(data, index):
    frequency = np.ones(len(data))
    cnt = 0
    for doc in data:
        for i, j in doc:
            if i == index:
                frequency[0] += j
        cnt += 1
    mean = np.mean(frequency)
    var = np.var(frequency)
    print('index', index)
    print('mean', mean)
    print('var', var)
    return mean, var

params = []
for i in range(10):
    params += static_single(data, i)
for i in params:
    print(i)
