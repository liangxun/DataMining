import pickle as pkl
import numpy as np
from scipy import sparse
from sklearn import metrics

len_features = 5000

with open('./data/tfidf{}_train.pkl'.format(len_features), 'rb') as f:
    tfidf = pkl.load(f)
y = np.load('./data/y_train.npy')
assert tfidf.shape[0] == y.shape[0]

# ============== 计算条件概率 ==============
scores = np.ones((len(np.unique(y)), tfidf.shape[1]))
for i in range(len(y)):
    doc = tfidf[i].toarray().flatten()
    scores[y[i]] += doc
rowsum = scores.sum(1)
r_inv = np.power(rowsum, -1).flatten()
r_mat_inv = sparse.diags(r_inv)
scores = np.log(r_mat_inv.dot(scores))
print('saving NBscores_{}.npy'.format(len_features))
np.save('./data/NBscores_{}.npy'.format(len_features), scores)

# ============= predict ==============
y_pred = []
for doc in tfidf:
    doc = doc.toarray().flatten()
    tmp = scores.dot(doc)
    y_pred.append(tmp.argmax())
print(metrics.accuracy_score(y, y_pred))
print(metrics.confusion_matrix(y, y_pred))

