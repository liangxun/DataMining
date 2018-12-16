import os
import pickle
import numpy as np
from gensim import corpora, models
from loadFile import load_file


def build_dictionary(corpus, len_dict, dir='./data/'):
    if os.path.exists('{}dictionary{}.dict'.format(dir, len_dict)):
        print('load exiting dictionary from {}bow{}.mm'.format(dir, len_dict))
        dictionary = corpora.Dictionary.load('{}dictionary{}.dict'.format(dir, len_dict))
    else:
        dictionary = corpora.Dictionary(corpus)

        # 1.去掉出现次数低于no_below的
        # 2.去掉出现次数高于no_above的。注意这个小数指的是百分数
        # 3.在1和2的基础上，保留出现频率前keep_n的单词
        dictionary.filter_extremes(keep_n=len_dict)
        print('saving dictionary from {}bow{}.mm'.format(dir, len_dict))
        dictionary.save('{}dictionary{}.dict'.format(dir, len_dict))

    return dictionary


# ====================== Bag of Words =======================
def build_bow(corpus, dictionary, dir='./data/', suffix='train'):
    """
    通过下面一句得到语料中每一篇文档对应的稀疏向量（这里是bow向量） 即 词袋模型
    向量的每一个元素代表了一个word在这篇文档中出现的次数
    :param corpus:
    :param dictionary:
    :return:
    """
    if os.path.exists('{}bow{}_{}.mm'.format(dir, len(dictionary), suffix)):
        print('load exiting bow from {}bow{}_{}.mm'.format(dir, len(dictionary), suffix))
        bow = corpora.MmCorpus('{}bow{}_{}.mm'.format(dir, len(dictionary), suffix))
    else:
        bow = [dictionary.doc2bow(doc) for doc in corpus]
        corpora.MmCorpus.serialize('{}bow{}_{}.mm'.format(dir, len(dictionary), suffix), bow)
    return bow

'''
# ====================== TF-IDF =======================
def build_tfidf(corpus, dictionary, dir='./data/', suffix='train'):
    if os.path.exists('{}tf_idf{}_{}.pkl'.format(dir, len(dictionary), suffix)):
        print('load exiting bow from {}tf_idf{}_{}.pkl'.format(dir, len(dictionary), suffix))
        with open('{}tf_idf{}_{}.pkl'.format(dir, len(dictionary), suffix), 'rb') as f:
            corpus_tfidf = pickle.load(f)
    else:
        bow = build_bow(corpus, dictionary, dir)
        model = models.TfidfModel(bow)
        corpus_tfidf = model[bow]
        with open('{}tf_idf{}_{}.pkl'.format(dir, len(dictionary), suffix), 'wb') as f:
            pickle.dump(corpus_tfidf, f)
    return corpus_tfidf
'''

if __name__ == '__main__':
    len_dictionary = 10000
    x_train, y_train, x_test, y_test = load_file(dir='./data/new_cuted_all_data/')
    dictionary = build_dictionary(x_train, len_dictionary)
    bow = build_bow(x_train, dictionary)
    print('bow', type(bow), len(bow))
    y_train = np.array(y_train)
    np.save('./data/y_train.npy', y_train)
    y_test = np.array(y_test)
    np.save('./data/y_test.npy', y_test)
