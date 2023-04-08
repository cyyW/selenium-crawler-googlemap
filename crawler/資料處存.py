# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 21:16:57 2022

@author: USER
"""

import numpy as np
import pandas as pd
import re
'''
data_dict = {'時間':dict_month,
             '星數':dict_star,}

dict_message1 = pd.DataFrame({'留言':dict_message}).replace('',np.nan)
print(dict_message1)

dict_tag1 = pd.DataFrame({'讚數':dict_tag}).replace('', 0)
print(dict_tag1)

print(range(len(dict_month)))
print(range(len(dict_star)))
print(range(len(dict_tag1)))
print(range(len(dict_message1)))
 

ddata_dict = pd.DataFrame(data_dict)
print(ddata_dict)

ddata_dict1 = pd.concat([ddata_dict, dict_tag1, dict_message1],axis=1)
print(ddata_dict1)

ddata_dict2 = ddata_dict1.dropna(axis='index', how='any', subset=['留言']).reset_index(drop=True)
print(ddata_dict2)


ddata_dict2.to_excel("wc1.xlsx",index = False, header = False)

driver.close()
'''
'''
df1 = pd.read_excel("tp.xlsx",index_col=0,engine="openpyxl")
df2 = pd.read_excel("newtp.xlsx",index_col=0,engine="openpyxl")
df3 = pd.read_excel("Takao.xlsx",index_col=0,engine="openpyxl")
print(df1)
print(df2)
print(df3)
res = pd.concat([df1,df2,df3],axis=0, ignore_index=True)
print(res)
res.to_excel('tptptk.xlsx',engine='xlsxwriter',index = False, header = False)
'''

df1 = pd.read_excel("tptptk.xlsx",index_col=0,engine="openpyxl")
print(df1)
train = []
label = []

#過濾資料放入list
for x in range(len(df1)):
    result = re.sub(r'[^\u4e00-\u9fff]', '', str(df1.iat[x,2]))  
    train.append(result)
for y in range(len(df1)):
    label.append(int(str(df1.iat[y,0]).replace('1','0').replace('2','0').replace('3','0').replace('5','1').replace('4','1')))


#去除空留言(df_mix1)
df_train = pd.DataFrame({'train':train}).replace('',np.nan)
print(df_train)
df_label = pd.DataFrame({'label':label})
print(df_label)
df_mix = pd.concat([df_train, df_label],axis=1)
print(df_mix)
df_mix1 = df_mix.dropna(axis='index', how='any', subset=['train']).reset_index(drop=True)
print(df_mix1)
print("資料長度:",len(df_mix1))


#分別取得正負評後垂直合併(df_mix2)(正隨機取5000、負3000)
df_p = df_mix1.query("label > 0").reset_index(drop=True)
print("資料長度:",len(df_p))
df_p = df_p.sample(5000).reset_index(drop=True)
print("所有正評")
print("資料長度:",len(df_p))
print(df_p)

df_n = df_mix1.query("label < 1").reset_index(drop=True)
print("資料長度:",len(df_n))
df_n = df_n.sample(3000).reset_index(drop=True)
print("所有負評")
print("資料長度:",len(df_n))
print(df_n)

df_mix2 = pd.concat([df_n, df_p],axis=0, ignore_index=True)
print("大整理")
print(df_mix2)

df_mix2.to_excel('tptptkclean2.xlsx',engine='xlsxwriter')














