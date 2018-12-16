## Bag of Words
<type: gensim.corpora.mmcorpus.MmCorpus>    <br>
bow10000_train.mm   <br>
bow10000_test.mm    <br>

## TF-IDF
<type: scipy.sparse.csr.csr_matrix>     <br>
tfidf5000_test.pkl      <br>
tfidf5000_train.pkl     <br>


## true catagory labels
y_train.npy <br>
y_test.npy  <br>

# NBscores_5000.npy
## other files
new_cuted_all_data/ &emsp; 分词之后的原始语料    <br>
dictionary10000.dict    &emsp;  建立bow使用的词典  <br>
ch2_scores(10000to5000).pkl    &emsp;  卡方检验的值（10000维降到5000维)    <br>
NBscores_5000.npy    &emsp;  朴素贝叶斯的先验概率    <br>