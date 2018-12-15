import os
import pickle as pkl
import numpy as np
import multiprocessing


# ====================== load data ==============


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


def static_per_catagory(corpus, dictionary, catagory_index, catagorys):
    """
    Conditional Probability P(X|Y=catagory_index)
    :param corpus:
    :param dictionary:
    :param catagory_index:
    :return:
    """
    cp_catagory = []
    print("{} contrains {} docs".format(catagorys[catagory_index], len(corpus)))
    with open('./data/static/{}.txt'.format(catagory_index), 'wb') as f:
        for token, id in dictionary.token2id.items():
            mean, var = static_per_word(corpus, id)
            print('{}(id={}): mean={}, var={}'.format(token, id, mean, var))
            cp_catagory.append((id, mean, var))
            f.write('{}(id={}): mean={}, var={}\n'.format(token, id, mean, var))
    with open('./data/static/{}.pkl'.format(catagory_index), 'wb') as f:
        pkl.dump(cp_catagory, f)


def static(corpus, dictionary, catagorys):
    assert len(corpus) % len(catagorys) == 0
    int_v = int(len(corpus) / len(catagorys))
    p = multiprocessing.Pool()
    for i in range(len(catagorys)):
        print("Computing P(X|Y='{}')".format(catagorys[i]))
        p.apply_async(static_per_catagory, args=(corpus[int_v*i:int_v*(i+1)], dictionary, i, catagorys))
    p.close()
    p.join()
    print('done')


if __name__ == '__main__':
    len_dictionary = 5000
    from BowGensim import build_dictionary, build_tfidf
    dictionary = build_dictionary(corpus=None, len_dict=len_dictionary)
    tf_idf = build_tfidf(corpus=None, dictionary=dictionary)
    print(len(tf_idf), type(tf_idf))
    y_train = np.load('./data/y_train.npy')
    print('y_train', y_train.shape)
    from loadFile import catagorys
    static(tf_idf, dictionary, catagorys)
