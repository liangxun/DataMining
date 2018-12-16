import pickle as pkl
import numpy as np
from sklearn.svm import LinearSVC, SVC
from sklearn import metrics


# ============= training svm models =============
def linersvm(x, y, model_dir='./linersvm.pkl'):
    clf = LinearSVC()
    clf.fit(x, y)

    with open(model_dir, 'wb') as f:
        pkl.dump(clf, f)

    y_pred = clf.predict(x)
    print('the metrics of linersvm on train set: ')
    print(metrics.accuracy_score(y, y_pred))
    print(metrics.confusion_matrix(y, y_pred))


def svm(x, y, model_dir='./svm.pkl'):
    clf = SVC()
    clf.fit(x, y)

    with open(model_dir, 'wb') as f:
        pkl.dump(clf, f)

    y_pred = clf.predict(x)
    print('the metrics of svm on train set: ')
    print(metrics.accuracy_score(y, y_pred))
    print(metrics.confusion_matrix(y, y_pred))


if __name__ == '__main__':
    len_features = 5000

    with open('./data/tfidf{}_train.pkl'.format(len_features), 'rb') as f:
        tfidf = pkl.load(f)
    y = np.load('./data/y_train.npy')
    assert tfidf.shape[0] == y.shape[0]

    # linersvm(tfidf, y, model_dir='./data/linersvm{}.pkl'.format(len_features))
    svm(tfidf, y, model_dir='./data/svm{}.pkl'.format(len_features))






