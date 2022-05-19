import requests

url = 'https://tw.stock.yahoo.com/quote/00632R.TW'  
web = requests.get(url)
web.encoding = 'utf-8'
ts= web.text.split('\n')
for t in ts:
    try:
        a= t.split(',')
        print(a[0],':',a[12])
    except:
        break