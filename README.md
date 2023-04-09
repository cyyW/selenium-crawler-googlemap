# selenium-crawler-googlemap

mix.py 是一個透過 selenium 爬取 google map 中評論的時間、讚數、星數及留言等資訊的 python 程式碼

資料處存.py 則是將 tptptk.xlsx 的資料清洗及整理成如 tptptkclean2.xlsx 中的狀態

# 環境

python 3.9.15

chrome driver:https://chromedriver.chromium.org/downloads

# 故障

mix.py 抓取評論星數的功能因 google map 改版暫時無法使用
 
mix.py 如若無法順利運行請自行檢查 driver.find_element By.XPATH 中的 FULL XPATH 於 google map 中是否有更動並請自行替換

  
  
