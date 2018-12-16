"""
Bog of Words
"""
import os
import numpy as np
from gensim import corpora
from loadFile import load_file


def build_dictionary(corpus, len_dict, dir='./data/'):
    """
    从语料中建立词典
    :param corpus: 语料（分词之后的）
    :param len_dict: 指定词典的大小
    :param dir: 生成的词典将要保存的位置
    :return: 词典对象
    """
    if os.path.exists('{}dictionary{}.dict'.format(dir, len_dict)):
        print('load exiting dictionary from {}bow{}.mm'.format(dir, len_dict))
        dictionary = corpora.Dictionary.load('{}dictionary{}.dict'.format(dir, len_dict))
    else:
        dictionary = corpora.Dictionary(corpus)
        dictionary.filter_extremes(keep_n=len_dict)
        print('saving dictionary to {}dictionary{}.dict'.format(dir, len_dict))
        dictionary.save('{}dictionary{}.dict'.format(dir, len_dict))

    return dictionary


# ====================== Bag of Words =======================
def build_bow(corpus, dictionary, dir='./data/', suffix='train'):
    """
    通过下面一句得到语料中每一篇文档对应的稀疏向量（这里是bow向量） 即 词袋模型
    向量的每一个元素代表了一个word在这篇文档中出现的次数
    :param corpus: 语料
    :param dictionary: 词典
    :return: 词袋bow
    """
    if os.path.exists('{}bow{}_{}.mm'.format(dir, len(dictionary), suffix)):
        print('load exiting bow from {}bow{}_{}.mm'.format(dir, len(dictionary), suffix))
        bow = corpora.MmCorpus('{}bow{}_{}.mm'.format(dir, len(dictionary), suffix))
    else:
        bow = [dictionary.doc2bow(doc) for doc in corpus]
        print('saving bow to {}bow{}_{}.mm'.format(dir, len(dictionary), suffix))
        corpora.MmCorpus.serialize('{}bow{}_{}.mm'.format(dir, len(dictionary), suffix), bow)
    return bow


if __name__ == '__main__':
    len_dictionary = 10000
    x_train, y_train, x_test, y_test = load_file(dir='./data/new_cuted_all_data/')
    dictionary = build_dictionary(x_train, len_dictionary)
    train_bow = build_bow(x_train, dictionary, suffix='trian')
    print('bow', type(train_bow), len(train_bow))
    test_bow = build_bow(x_test, dictionary, suffix='test')
    print('bow', type(test_bow), len(test_bow))
    y_train = np.array(y_train)
    np.save('./data/y_train.npy', y_train)
    y_test = np.array(y_test)
    np.save('./data/y_test.npy', y_test)
