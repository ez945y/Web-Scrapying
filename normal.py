import requests
from bs4 import BeautifulSoup
requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.proxies = {"https": "117.184.11.82:8080", "http": "36.248.10.47:8080", }
s.keep_alive = False 
web = s.get('https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html', cookies={'over18':'1'})
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')
name = 0    #  設定圖片編號
for i in imgs:
  print(i['src'])
  jpg = s.get(i['src'])     # 使用 requests 讀取圖片網址，取得圖片編碼
  f = open(f'C:\\Users\\admin\\Desktop\\visual env\\庫\\test_{name}.jpg', 'wb')    # 使用 open 設定以二進位格式寫入圖片檔案
  f.write(jpg.content)   # 寫入圖片的 content
  f.close()              # 寫入完成後關閉圖片檔案
  name = name + 1 