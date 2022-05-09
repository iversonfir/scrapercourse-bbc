import requests as req
from bs4 import BeautifulSoup as bs

resp=req.get('https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt')
soup=bs(resp.text,'lxml')
urls=soup.find_all('a',{'class':'qa-story-image-link'})
tag_list=[]
for url in urls:
    context='https://www.bbc.com'
    url=context+url.get('href')
    sub_resp=req.get(url)
    sub_soup=bs(sub_resp.text,'lxml')
    tags=sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
    for tag in tags:
        tag_list.append(tag.find('a').getText())
print(tag_list)

