import requests as req
from bs4 import BeautifulSoup as bs


resp=req.get('https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt')

soup=bs(resp.text,'lxml')
titles=soup.find_all('span',{'class':'lx-stream-post__header-text gs-u-align-middle'})
title_list=[]
for title in titles:
    title_list.append(title.getText())

print(title_list)