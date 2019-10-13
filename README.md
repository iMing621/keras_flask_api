# Simple Keras image predict API


## Introduction
這篇算是一個方便我之後查閱的學習筆記

如果你跟我一樣略懂 python 

很想試試看圖像辨識, 卻不知該從哪開始?

下面這個小程式, 應該會是個不錯的開始 : )


## Purpose
利用 Keras Pre-trained 模型 + Flask 建立 Restful API 

當使用者輸入圖片網址時, API 會回傳 json 格式的預測結果


## Preparation

以下版本只是我開發時所安裝的版本

若一律選擇安裝最新版, 應該不影響執行結果

另外, 由於我是利用 Anaconda 的虛擬環境進行開發

假如下面的清單有遺漏, 還請見諒.

### Env.
- Windows
- Anaconda3
- Python 3.6
- cURL win64 7.66.0

### Required Libs
- Flask==1.1.1
- Keras==2.2.4
- numpy==1.16.5
- Pillow==6.2.0
- requests==2.22.0
- tensorflow=1.13.1


## 開始囉~

以下內容若發現任何問題

建議參考 [Reference](reference.md)

### 1. 下載程式
下載相關程式到專案目錄下
- [app.py](app.py) (主程式)
- [requirements.txt](requirements.txt)

### 2. 建立並啟動虛擬環境
利用 **Anaconda Navigator** 
1. 開啟 Navigator
2. 按下下方 "Create" 按鈕, 建立虛擬環境
3. 確認虛擬環境列在 Environments 清單中
4. 按下三角形按鈕出現選單
5. 選擇 "Open Terminal"
6. 會出現一個類似命令提示字元的視窗

或是

1. 啟動 **Anaconda Prompt**
2. 輸入以下指令
```sh
$ conda create --name env4kerasApi python=3.6
```
 - `--name env4kerasApi` 虛擬環境名稱
 - `python=3.6` 指定安裝 python 版本

3. 接著輸入
```sh
$ activate env4kerasApi
```


### 3. 安裝套件
兩種方式擇一即可

#### 利用 requirements.txt 安裝
```sh
$ pip install -r requirements.txt
```

#### 參考 Required Libs 
```sh
$ conda install xxxxx
```


### 4. 啟動 server
在 **Anaconda Prompt** 輸入以下指令
```sh
$ python app.py
```

如果啟動成功的話, 應該會在 Anaconda Prompt 看到
```sh
$ python app.py
Using TensorFlow backend.
...
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

打開瀏覽器輸入 `http://127.0.0.1:5000/`

應該會看到 Hello Flask!!


### 5. 送出請求
打開命令提示字元, 利用 cURL 送出 POST
``` curl
$ curl -X POST -d "size=3" -d "img_path=圖片網址" http://localhost:5000/predict
```
* `size=數字` 是我自定義的的參數, 因為我想讓 user 自行決定回傳的預測結果數

或是參考 [這篇](https://github.com/jrosebr1/simple-keras-rest-api "這篇") 寫一隻簡單的 py 發 request


如果看到回傳
``` json
{
  "predictions": [
    {
      "label": "notebook",
      "probability": 35.99
    },
    {
      "label": "desktop_computer",
      "probability": 18.68
    },
    {
      "label": "laptop",
      "probability": 11.62
    }
  ],
  "success": true
}
```

恭喜你, 跨過了一個入門檻 (放煙火)
