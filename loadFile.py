import pickle
import random


catagorys = ['agriculture', 'car', 'computersoftware', 'finance', 'labor',
            'medical', 'movie', 'policy', 'psychology', 'sport']

random.seed(1)
len_split = 40000


def load_file(dir='./data/new_cuted_all_data/'):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for catagory in catagorys:
        with open(dir+'{}.txt'.format(catagory), 'rb') as f:
            data = pickle.load(f)
            print('catagory {} contain {} docs'.format(catagory, len(data)))
            assert len(data) > len_split * 2
            random.shuffle(data)
            train = data[:len_split]
            test = data[len_split: len_split*2]
            x_train += train
            y_train += [catagorys.index(catagory)] * len_split
            x_test += test
            y_test += [catagorys.index(catagory)] * len_split
    return x_train, y_train, x_test, y_test


if __name__ == '__main__':
    x_train, y_train, x_test, y_test = load_file()
    print(len(x_train))
    print(len(y_train))
    print(len(x_test))
    print(len(y_test))
