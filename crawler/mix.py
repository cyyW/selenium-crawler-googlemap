from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.action_chains import ActionChains
import logging
import numpy as np
import pandas as pd
import openpyxl
import xlsxwriter

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

driver=webdriver.Chrome(chrome_options=options)

driver.get('https://www.google.com.tw/maps/@25.0407284,121.5484174,15z?hl=zh-TW&authuser=0')
driver.maximize_window()

'''
alldata_dict = pd.DataFrame({'時間':[],
                             '星數':[],
                             '讚數':[],
                             '留言':[]})
'''
alldata_dict = pd.DataFrame({'時間':[],
                             '讚數':[],
                             '留言':[]})

time.sleep(2)

#搜尋關鍵字
searchbox = driver.find_element(By.ID, 'searchboxinput')
searchbox.send_keys('高雄 飲料')
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, 'searchbox-searchbutton')).click().perform()
time.sleep(3)


#滾動總店家頁面次數
for p in range (2) :
    pane0 = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane0)
    time.sleep(3)

x = 3
# actions.move_to_element(driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a')).click().perform()
#點擊店家數量
for y in range(2):
    dict_total = []
    dict_allstar = []
    dict_month = []
    dict_star = []
    dict_message = []
    dict_tag = []  
    try:
        #依序點擊店家、點擊更多評論、找到留言區介面
        actions.move_to_element(driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[' + str(x) + ']/div/a')).click().perform()
        time.sleep(5)
        #actions.move_to_element(driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[51]/div/button')).click().perform()
        actions.move_to_element(driver.find_element(By.CLASS_NAME,"M77dve ")).click().perform()
        time.sleep(5)
        x += 2
        scroll_div = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]')
       
        

        #下拉到最底
        '''
        all_window_height =  []  
        all_window_height.append(driver.execute_script("return document.body.scrollHeight;")) 
        while True:
            # actions.send_keys(Keys.PAGE_DOWN)
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_div)
            time.sleep(2)
            check_height = driver.execute_script("return document.querySelector('#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div:nth-child(9)').scrollHeight;")
            print("當前高度" + str(check_height))
            if check_height == all_window_height[-1]: 
                print("我已下拉完毕")
                break
            else:
                all_window_height.append(check_height) 
                print("我正在下拉")
        '''
        
        #留言頁面下拉，留言數量為(i+1)*10
        for i in range (2) :
            pane1 = driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]')
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane1)
            time.sleep(2)
        

        #抓取所需 enements
        months = driver.find_elements(By.CLASS_NAME,"rsqaWe")
        messages = driver.find_elements(By.CLASS_NAME,"wiI7pd")
        stars = driver.find_elements(By.CLASS_NAME,("kvMYJc"))
        tags = driver.find_elements(By.CLASS_NAME,"znYl0")
        fulltext= driver.find_elements(By.CLASS_NAME,"w8nwRe.kyuRq")
        
        #點開全部評論
        for ft in fulltext:
            ft.click()
            time.sleep(0.5)
        
        #抓取讚數
        z = 1
        for month in months:   
            # time.sleep(0.5)    
            try:                                               
                # map_review = driver.find_element(By.XPATH, ' /html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[9]/div[1]/div/div[3]/div[4]/div[8]/button[2]/span')
                dict_tag.append(int(driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[' + str(z) + ']/div/div/div[4]/div[5]/button[1]/span').get_attribute('textContent').replace('喜歡', '')))
                # print(str(w) + ' ' + '成功')
                # print(driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/div[' + str(z) + ']/div/div[3]/div[4]/div[8]/button[2]/span').get_attribute('textContent'))
                z += 3
            except:
                dict_tag.append("")
                # print(str(w) + ' ' + '失敗')
                z += 3

        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[' + str(z) + ']/div[2]/div[3]/div[4]/div[8]/button[2]/span
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[a]/div[2]/div[3]/div[4]/div[8]/button[2]/span
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[1]/div/div/div[4]/div[5]/button[1]
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[4]/div/div/div[4]/div[5]/button[1]
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[4]/div/div/div[4]/div[5]/button[1]
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[1]/div/div/div[4]/div[5]/button[1]/span
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[4]/div/div/div[4]/div[5]/button[1]/span
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[' + str(z) + ']/div/div/div[4]/div[5]/button[1]/span

        #抓取留言(透過時間迴圈篩出空白留言)
        s = 1
        w = 1
        for month in months:  
            try:
                dict_message.append(driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[' + str(s) + ']/div/div/div[4]/div[2]/div/span[1]').get_attribute('textContent').replace('\n', '').replace('�', '').replace('口', '').replace('👍', ''))
                print(str(w) + ' ' + '成功')
                # print(driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[9]/div[' + str(s) + ']/div/div[3]/div[4]/div[2]/span[2]').get_attribute('textContent'),"\n")
                s += 3
                w += 1                                    
            except:
                logging.exception("An exception was thrown!")
                print(str(w) + ' ' + '失敗')
                w += 1
                break
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[1]/div/div/div[4]/div[2]/div/span[1]
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[4]/div/div/div[4]/div[2]/div/span[1]
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[' + str(s) + ']/div/div/div[4]/div[2]/div/span[1] 
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[a]/div[2]/div[3]/div[4]/div[2]/div/span[2]
        #/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[3]/div[9]/div[' + str(s) + ']/div[2]/div[3]/div[4]/div[2]/div/span[2]           
        #總分及各星評論數
        '''
        totals = driver.find_element(By.CLASS_NAME, "jANrlb")
        # print("總分:",totals.get_attribute('textContent'),"\n")
        dict_total.append(totals.get_attribute('textContent'))

        allstars = driver.find_elements(By.CLASS_NAME,("BHOKXe"))
        # print("各星評論數:","\n")
        for allstar in allstars :  
            # print(allstar.get_attribute('aria-label'))
            dict_allstar.append(allstar.get_attribute('aria-label'))
        '''
        #抓取月份、星數
        for month in months: 
            # print(str(x) + ' ' + month.get_attribute('textContent'))
            dict_month.append(month.get_attribute('textContent'))
        print("月份成功")    
        '''
        for star in stars :            
            # print(star.get_attribute('aria-label'))
            dict_star.append(int(star.get_attribute('aria-label').replace('顆星', '')))      
        print("星數成功")
        '''
        #由於有不明原因導致少部分店家會有星數多抓，因此這裡先將每個店家的時間、留言、星數、讚數先進行 dataframe 合併，
        #沒問題刪除空白留言資料後併入 alldata_dict，並將有問題的店家排除
        try:
            data_dict = {'時間':dict_month}
            #'星數':dict_star

            dict_message1 = pd.DataFrame({'留言':dict_message}).replace('',np.nan)
            print(dict_message1)

            dict_tag1 = pd.DataFrame({'讚數':dict_tag}).replace('', 0)
            print(dict_tag1)

            ddata_dict = pd.DataFrame(data_dict)
            print(ddata_dict)

            ddata_dict1 = pd.concat([ddata_dict, dict_tag1, dict_message1],axis=1)
            print(ddata_dict1)

            ddata_dict2 = ddata_dict1.dropna(axis='index', how='any', subset=['留言']).reset_index(drop=True)
            print(ddata_dict2)

            alldata_dict = pd.concat([alldata_dict,ddata_dict2],axis=0,ignore_index = True )
            print("ok")
            print(alldata_dict)
            print("第",y+1,"家店")
        except:
            print("這一輪的店家出包了")
            print(range(len(dict_month)))
            #print(range(len(dict_star)))
            print(range(len(dict_tag1)))
            print(range(len(dict_message1)))
    except:
        #如果正常跑完不會出現
        print("沒店家了")
        break
    

print("共",y+1,"家店")
print("二次確認")
alldata_dict1 = pd.DataFrame(alldata_dict)
print(alldata_dict1)

#存檔(檔名)
'''
alldata_dict1.to_excel('Takao.xlsx',engine='xlsxwriter',index = False, header = False)
driver.close()
'''

'''
data_dict = {'時間':dict_month,
             '星數':dict_star,}

dict_message1 = pd.DataFrame({'留言':dict_message}).replace('',np.nan)
print(dict_message1)

dict_tag1 = pd.DataFrame({'讚數':dict_tag}).replace('', 0)
print(dict_tag1)

ddata_dict = pd.DataFrame(data_dict)
print(ddata_dict)

print(range(len(dict_month)))
print(range(len(dict_star)))
print(range(len(dict_tag1)))
print(range(len(dict_message1)))

ddata_dict1 = pd.concat([ddata_dict, dict_tag1, dict_message1],axis=1)
print(ddata_dict1)

ddata_dict2 = ddata_dict1.dropna(axis='index', how='any', subset=['留言']).reset_index(drop=True)
print(ddata_dict2)

res = pd.concat([alldata_dict,ddata_dict2],axis=0,ignore_index = True )

ddata_dict2.to_excel("wc1.xlsx",index = False, header = False)


'''


















