# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:56:39 2020

@author: 邹十二
"""



#导入模块
import requests
import json
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv
#UA伪装：将对应的User-Agent封装到一个字典中

proxy={
        "https": "127.0.0.1:15732",
        "http": "127.0.0.1:15732"
}
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/7.0.4280.67 Safari/537.36 Edg/87.0.664.55'}
#网页访问连接
url1='https://jandan.net'
url2='https://jandan.net/treehole'
url3='https://flowgpt.com/prompt/mQzEosdaqlUftU-PtKSEC?isModal=true'

url4='https://flowgpt.com/?sort=top'
url5='https://flowgpt.com/prompt/r_DuXTNElfua86QqAmHNV?isModal=true'




def chatpa(url3):
    r = requests.get(url3,headers=headers,proxies=proxy)
    #print(r.text)
    
    
    
    pattern1 = r"\"upvotes(.*?)\,\"" 
    pattern2 = r"\"upvotes.instructions"
    pattern3 = r"\"initPrompt(.*)instructions" 
    pattern4 = r"\"Read(.*)\"live\":true" 
    
    
    pattern5 = r"\"initPrompt.*?\,\"" 
    #提示词
    pattern6 = r"\"content.*?patient" 
    
    #评论
    pattern7 = r"<title>.*?<" 
    
    match1 = re.search(pattern7, r.text)
    title=match1.group()[7:-1]
    match2 = re.search(pattern5, r.text)
    prompt=match2.group()[14:-7]
    
    prompt=prompt.replace("\\n","")
    prompt=prompt.replace("\\","")
    content=r.text.split("\"role\"")
    
    con=content[1][2:-4]
    con=con.replace("\\n","")
    con=con.replace("\\n\n","")
    con=con.replace("\\","")
#    print(con)

    #评论五条
    match3 = re.search(pattern1, r.text)
    upv=match3.group()[10:-2]
    
#    print(title) 
#    print(upv) 
#    print(prompt) 
    
    with open('C:/Users/邹十二/Desktop/data.csv','a',encoding='gb18030',newline='') as afile:
        csv_writer = csv.writer(afile)
        csv_writer.writerow([title,upv,prompt,con])


#chatpa('https://flowgpt.com/prompt/o97aOL86cnIw2zWrEaHKG?isModal=true')
k=0
with open('C:/Users/邹十二/Desktop/topurl.txt') as file:
    
    
    for item in file.readlines()[0:50]:#从第n行继续爬取
        
        print(item)
        try:
            
            chatpa(item)
        except:
            
            pass
            continue    
                
        k=k+1 
        if k>40:
            break
        
    
    
    
    
       
        
        
        
        
        
        