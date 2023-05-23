# selenium-crawler-google map
此項目是透過 python selenium 自動化蒐集 google map 上的資料，並進行初步的資料整理後提供給 [LSTM_Sentiment-Analysis_zh-tw](https://github.com/cyyW/LSTM_Sentiment-Analysis_zh-tw#lstm_sentiment-analysis_zh-tw) 進行 LSTM
情緒分析訓練。

crawler 中包含兩個檔案 :

1. [mix.py](https://github.com/cyyW/selenium-crawler-googlemap/blob/master/crawler/mix.py) 透過 selenium 爬取 google map 中評論的時間、讚數、星數及留言資訊，過程使用 pandas 去除空白留言資料並存入 Excel 之中。

2. [資料處存.py](https://github.com/cyyW/selenium-crawler-googlemap/blob/master/crawler/%E8%B3%87%E6%96%99%E8%99%95%E5%AD%98.py) 則是將 [tptptk.xlsx](https://github.com/cyyW/selenium-crawler-googlemap/blob/master/crawler/tptptk.xlsx) 的資料清洗及整理成如 [tptptkclean2.xlsx](https://github.com/cyyW/selenium-crawler-googlemap/blob/master/crawler/tptptkclean2.xlsx) 中的狀態。
   - 過濾留言中中文以外的字詞，將星數進行正負面分類
   - 去除空白留言資料
   - 隨機取正向資料5000、負向資料3000存入 [tptptkclean2.xlsx](https://github.com/cyyW/selenium-crawler-googlemap/blob/master/crawler/tptptkclean2.xlsx)


## 環境

* python `3.9.15`
* 虛擬環境使用 `conda`
* chrome driver : https://chromedriver.chromium.org/downloads

## 使用

* [mix.py](https://github.com/cyyW/selenium-crawler-googlemap/blob/master/crawler/mix.py) 抓取評論星數的功能因 google map 改版暫時無法使用
 
* [mix.py](https://github.com/cyyW/selenium-crawler-googlemap/blob/master/crawler/mix.py) 如若無法順利運行請自行檢查 driver.find_element By.XPATH 中的 FULL XPATH 於 google map 中是否有更動並請自行替換

  
  
