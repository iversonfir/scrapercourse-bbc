import grequests as req
from bs4 import BeautifulSoup as bs
import time

start_time=time.time()
links=[f'https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt/page/{page}' for page in range(1,4)]
reqs=(req.get(link) for link in links)
resps=req.imap(reqs,req.Pool(3))
for index,resp in enumerate(resps):
    soup=bs(resp.text,'lxml')
    titles=soup.find_all('a',{'qa-heading-link lx-stream-post__header-link'})
    title_list=[]
    for title in titles:
        title_list.append(title.getText()) 
    
    context='https://www.bbc.com'
    urls=soup.find_all('a',{'class':'qa-story-image-link'})
    url_list=[]
    sub_links=[f'{context}'+url.get('href') for url in urls]
    sub_reqs=(req.get(sub_link) for sub_link in sub_links)
    sub_resps=req.imap(sub_reqs,req.Pool(10))
    
    tag_list=[]
    for sub_resp in sub_resps:
        sub_soup=bs(sub_resp.text,'lxml')
        tags=sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
        for tag in tags:
            tag_list.append(tag.find('a').getText())
    print(f'第{index+1}頁')
    print('標題')
    print(title_list)
    print('標籤')
    print(tag_list)

end_time=time.time()
print(f'花費{end_time-start_time}秒')