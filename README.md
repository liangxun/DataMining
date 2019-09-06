# 北邮计算机研一《数据挖掘》文本分类实验
<hr>

## 数据集
从知网爬取了100W篇文章摘要  
共10个类，每一类10W条数据

## 分类算法
NaiveBayes  (numpy实现)  
SVM （sklearn实现）
<hr>

## files description
- `CNKI/` 爬虫部分，使用scrapy框架  
- `data/` 原始数据，bow，tf_idf, 模型参数等  
- `notebook/report.ipynb`  实验报告，测试集结果
