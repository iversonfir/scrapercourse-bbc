import requests as req
from bs4 import BeautifulSoup as bs

for page in range(1,4):
    resp=req.get(f'https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt/page/{page}')
    soup=bs(resp.text,'lxml')
    urls=soup.find_all('a',{'class':'qa-story-image-link'})
    titles=soup.find_all('a',{'qa-heading-link lx-stream-post__header-link'})
    title_list=[]
    tag_list=[]
    for title in titles:
        title_list.append(title.getText())
    
    
    for url in urls:
        context='https://www.bbc.com'
        url=context+url.get('href')
        sub_resp=req.get(url)
        sub_soup=bs(sub_resp.text,'lxml')
        tags=sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
        for tag in tags:
            tag_list.append(tag.find('a').getText())
    print(f'page 第{page}頁')
    print('標題')
    print(title_list)
    print('標籤')
    print(tag_list)
    
    
