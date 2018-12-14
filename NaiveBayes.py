# 参考 https://github.com/Zephery/weiboanalysis/blob/master/Bayes.py
# 把一类文档看成一种分布，通过衡量两个分布之间的相似度
# 这种方法其实并不是典型的Bayes


import numpy as np
from gensim import corpora
from itertools import islice
import pickle as pkl
from sklearn import metrics

len_dictionary = 5000

'''
corpus = corpora.MmCorpus('./data/corpuse.mm')
# 拆分成10个文件,每个类有5W个文档
int_v = 50000
params = []
for label in range(10):
    data = []
    start = label * int_v
    end = (label+1) * int_v
    for doc in islice(corpus, start, end):
        data.append(doc)
    with open('./data/corpus_{}.mm'.format(label), 'wb') as f:
        pkl.dump(data, f)
'''



corpus = corpora.MmCorpus('./data/corpuse.mm')


def trainingNaiveBayes(corpus, label, start):  # 计算先验概率
    """计算条件概率和先验概率"""
    numWords = len_dictionary

    words = np.ones(numWords)
    WordsNum = 2.0  # 如果一个概率为0，乘积为0，故初始化1，分母2

    cnt = start
    for doc in corpus:
        print('doc index:', cnt)
        cnt += 1
        # print(doc)
        # print('len(doc)', len(doc))
        for i, j in doc:
            # print(i, j)
            words[i] += j
            WordsNum += j

    words = words[:]
    P_Words = words / WordsNum

    return P_Words, label


int_v = 50000
params = []
for label in range(10):
    start = label * int_v
    end = (label+1) * int_v
    # print(start, end)
    p, catagory = trainingNaiveBayes(islice(corpus, start, end), label, start)
    print(catagory)
    print(p)
    print(p.shape)
    params.append((catagory, p))

with open('./data/params_{}.pkl'.format(len_dictionary), 'wb') as f:
    pkl.dump(params, f)

'''
# 预测
with open('./data/params.pkl', 'rb') as f:
    params = pkl.load(f)
'''


def _pred(doc, params):
    test = np.zeros(len_dictionary)
    for i, j in doc:
        test[i] = j
    scores = []
    for y, distribution in params:
        score = np.sum(test * distribution)
        scores.append(score)
    y_pred = scores.index(max(scores))
    return y_pred


def predict(corpus, params):
    y_prediction = []
    cnt = 0
    for doc in corpus:
        y_pred = _pred(doc, params)
        y_prediction.append(y_pred)
        print('doc {}: pred = {}'.format(cnt, y_pred))
        cnt += 1

    return np.array(y_prediction)


corpus = corpora.MmCorpus('./data/corpuse.mm')
y_true = np.load('./data/tmp.npy')
y_pred = predict(corpus, params)

print(metrics.accuracy_score(y_true, y_pred))
print(metrics.confusion_matrix(y_true, y_pred))
np.save('./data/y_pred{}.npy'.format(len_dictionary), y_pred)


