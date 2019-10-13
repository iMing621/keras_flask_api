## Reference

### 程式參考
* 深度學習 入門教室 (p.89-90 Dogs+vs.+Cat.py)
  * [作者網站](http://www.sotechsha.co.jp/sp/1187/), 可下載程式碼, 勘誤表

* [Building a simple Keras + deep learning REST API](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)
  * [Source code](https://github.com/jrosebr1/simple-keras-rest-api)
  * 使用 ResNet50 model 預測, 很詳細的說明

* [Python Flask + Keras 建置圖片分類 API](https://blog.techbridge.cc/2018/11/01/python-flask-keras-image-predict-api/)
  * 基本上跟上一篇一樣, 只是有加上初始化 graph

* https://github.com/tech-quantum/sia-cog/blob/master/vis/objcls.py
  * 利用 Requests 下載圖片, 提供多種模型 (ResNet50, VGG16, VGG19, InceptionV3, Xception)

### Flask 相關
* [輕鬆學習 Python：使用 Flask 創建 Web API](https://medium.com/datainpoint/flask-web-api-quickstart-3b13d96cccc2)
  * Flask Restful API 基本範例

* [簡單的GET和Post方法取得Flask網頁資料](https://www.maxlist.xyz/2019/03/17/flask-get-post/)

### PIL 
* [以 Python Imaging Library 進行影像資料處理](https://yungyuc.github.io/oldtech/python/python_imaging.html)
  * 可以獲得更多 PIL 的說明, 對圖片做進階處理

### Keras
* [Keras 中文 API - Application 應用](https://keras-cn.readthedocs.io/en/latest/other/application/)

### Keras 模型
* [2018 iT邦幫忙鐵人賽 - AI & ML - Day 09 : CNN 經典模型應用](https://ithelp.ithome.com.tw/articles/10192162)
  * 多個模型的介紹, 若想微調 Model 的設定, 此文有說明

### cURL

cURL 下載後只需解壓縮, 位置可自行決定

exe 檔放在 System32 只是方便不需設定 Path 環境變數可隨處執行, 不需到該解壓縮目錄下執行

* [cURL Download 頁](https://curl.haxx.se/download.html)

* [IT邦幫忙鐵人賽 - Day14 - cURL 工具 (下載, 安裝)](https://ithelp.ithome.com.tw/articles/10185923)

* [Curl 常用指令整理](http://perrywu0606.pixnet.net/blog/post/16993042)

* [使用 curl指令測試REST服務](http://blog.kent-chiu.com/2013/08/14/testing-rest-with-curl-command.html)

### Anaconda
* [用conda建立及管理python虛擬環境](https://medium.com/python4u/%E7%94%A8conda%E5%BB%BA%E7%AB%8B%E5%8F%8A%E7%AE%A1%E7%90%86python%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83-b61fd2a76566)

----

## Issue
### Error 1
`ImportError('Could not import PIL.Image. ' working with keras-ternsorflow`

解法

安裝正確的 lib -> pillow

[來源](https://stackoverflow.com/questions/48225729/importerrorcould-not-import-pil-image-working-with-keras-ternsorflow/50775336)

### Error 2
`Tensor Tensor(“predictions/Softmax:0”, shape=(?, 1000), dtype=float32) is not an element of this graph`

#### 解法 1 
``` python
import tensorflow as tf
...
graph = tf.get_default_graph()
...
with graph.as_default():
    preds = model.predict(image) # 把原本執行取出特徵值的程式碼, 移到迴圈內執行
...
```
**來源**
1. https://github.com/jrosebr1/simple-keras-rest-api/issues/7
2. https://github.com/keras-team/keras/issues/2397
3. https://justttry.github.io/justttry.github.io/not-an-element-of-Tensor-graph/


#### 解法 2

clean .keras 資料夾內的 cache

沒試過, 不確定有沒有辦法解決

**來源**
https://stackoverflow.com/questions/53391618/tensor-tensorpredictions-softmax0-shape-1000-dtype-float32-is-not-an
