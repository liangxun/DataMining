import os
import pickle as pkl
import numpy as np
from BowGensim import build_dictionary, build_tfidf
from sklearn import metrics
from loadFile import catagorys


# ====================== load data ==============
len_dictionary = 5000
dictionary = build_dictionary(corpus=None, len_dict=len_dictionary)
tf_idf = build_tfidf(corpus=None, dictionary=dictionary)
print(len(tf_idf), type(tf_idf))
y_train = np.load('./data/y_train.npy')
print('y_train', y_train.shape)


# ===================== 计算条件概率 =============
def static_per_word(data, word_index):
    """

    :param data:
    :param word_index:
    :return:
    """
    frequency = np.ones(len(data))
    cnt = 0
    for doc in data:
        for i, j in doc:
            if i == word_index:
                frequency[0] += j
        cnt += 1
    mean = np.mean(frequency)
    var = np.var(frequency)
    return mean, var


def static_per_catagory(corpus, dictionary, catagory_index):
    """
    Conditional Probability P(X|Y=catagory_index)
    :param corpus:
    :param dictionary:
    :param catagory_index:
    :return:
    """
    cp_catagory = []
    for token, id in dictionary.token2id.items():
        mean, var = static_per_word(corpus, id)
        print('{}(id={}): mean={}, var={}'.format(token, id, mean, var))
        cp_catagory.append((id, mean, var))
    return cp_catagory


def static(corpus, dictionary, catagorys):
    if os.path.exists('./data/GNB_static.pkl'):
        with open('./data/GNB_static.pkl', 'rb') as f:
            cp_catagorys = pkl.load(f)
    else:
        assert len(corpus) % len(catagorys) == 0
        int_v = int(len(corpus) / len(catagorys))
        cp_catagorys = []
        for i in range(len(catagorys)):
            print("Computing P(X|Y='{}')".format(catagorys[i]))
            cp_catagory = static_per_catagory(corpus=corpus[int_v*i:int_v*(i+1)], dictionary=dictionary, catagory_index=i)
            cp_catagorys.append((i, cp_catagory))
        with open('./data/GNB_static.pkl', 'wb') as f:
            pkl.dump(cp_catagorys, f)
    return cp_catagorys


if __name__ == '__main__':
    static(tf_idf, dictionary, catagorys)
