import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
stock_urls = [
  'https://tw.stock.yahoo.com/quote/2330',
  'https://tw.stock.yahoo.com/quote/0050',
  'https://tw.stock.yahoo.com/quote/2317',
  'https://tw.stock.yahoo.com/quote/6547'
]

def getStock(url):
    web = requests.get(url)                          # 取得網頁內容
    soup = BeautifulSoup(web.text, "html.parser")    # 轉換內容
    title = soup.find('h1')             # 找到 h1 的內容
    a = soup.select('.Fz\(32px\)')[0]
    b = soup.select('.Fz\(20px\)')[0] 
    try:
      if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C($c-trend-down)'):
        s = '-'
    except:
        try:
            if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C($c-trend-up)')[0]:
                s = '+'
        except:
            s = '-'
    print(f'{title.get_text()} : {a.text} ({s}{b.text})')   # 印出結果
    
with ThreadPoolExecutor() as executor:
    executor.map(getStock, stock_urls)