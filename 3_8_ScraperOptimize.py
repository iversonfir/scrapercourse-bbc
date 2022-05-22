import requests as req
from bs4 import BeautifulSoup as bs
import time
import concurrent.futures

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

def scraper(links):
    resp=req.get(links,headers=headers,timeout=5)
    if(resp.status_code==200):
        soup=bs(resp.text,'lxml')

        titles=soup.find_all('a',{'qa-heading-link lx-stream-post__header-link'})
        if(titles):
            title_list=[]
            for title in titles:
                title_list.append(title.getText())
            print('標題')
            print(title_list)
        else:
            print("元素不存在")
    else:
        print("狀態碼非200")


start_time=time.time()
try:
    links=[f'https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt/page/{page}' for page in range(1,4)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(scraper,links)
except Exception as e:
    print(str(e))
end_time=time.time()

print(f'花費{end_time-start_time}秒')