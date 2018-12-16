## Bag of Words
<type: gensim.corpora.mmcorpus.MmCorpus>  
bow10000_train.mm  
bow10000_test.mm  

## TF-IDF
<type: scipy.sparse.csr.csr_matrix>  
tfidf5000_test.pkl  
tfidf5000_train.pkl  


## true catagory labels
y_train.npy  
y_test.npy  


## other files
new_cuted_all_data/ &emsp; 分词之后的原始语料  
dictionary10000.dict    &emsp;  建立bow使用的词典  
ch2_scores(10000to5000).pkl    &emsp;  卡方检验的值（10000维降到5000维)  
NBscores_5000.npy    &emsp;  朴素贝叶斯的先验概率  