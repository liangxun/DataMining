import pickle
from gensim import corpora, models
from loadFile import load_file

len_dictionary = 5000
x_train, y_train, x_test, y_test = load_file(dir='./data/new_cuted_all_data/')


def build_dictionary(corpus, len_dict, is_save=False):
    dictionary = corpora.Dictionary(x_train)

    # 1.去掉出现次数低于no_below的
    # 2.去掉出现次数高于no_above的。注意这个小数指的是百分数
    # 3.在1和2的基础上，保留出现频率前keep_n的单词
    dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=len_dict)
    if is_save is True:
        dictionary.save('corpora.dict')
    # dictionary = corpora.Dictionary.load('corpora.dict')  #加载方法
    return dictionary


# ====================== Bag of Words =======================
def bow(corpus, dictionary, is_save=False):
    """
    通过下面一句得到语料中每一篇文档对应的稀疏向量（这里是bow向量） 即 词袋模型
    向量的每一个元素代表了一个word在这篇文档中出现的次数
    :param corpus:
    :param dictionary:
    :return:
    """
    bow = [dictionary.doc2bow(doc) for doc in corpus]
    if is_save is True:
        corpora.MmCorpus.serialize('bow{}.mm'.format(len(dictionary)), bow)
    # bow = corpora.MmCorpus('bow{}.mm'.format(len(dictionary)))    #加载方法
    return bow


# ====================== TF-IDF =======================
def tf_idf(corpus, dictionary, is_save=False):
    corpus = bow(corpora, dictionary, is_save)
    model = models.TfidfModel(corpus)
    corpus_tfidf = model[corpus]
    if is_save is True:
        file = open('file.pkl', 'wb')
        pickle.dump(corpus_tfidf, file)
    return corpus_tfidf


if __name__ == '__main__':
    pass
