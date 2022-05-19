import requests
web = requests.get('https://today.line.me/tw/v2/article/oqay0ro')
id = web.text.split('<script>')[1].split('id:"article:')[1].split(':')[0]
comment = requests.get(f'https://today.line.me/webapi/comment/list?articleId={id}&sort=POPULAR&direction=DESC&country=TW&limit=30&pivot=0&postType=Article')
json = comment.json()
num = int(json['result']['comments']['count'])
print(num)
def getC(n):
  # 使用字串格式化的方式，讓網址會根據不同的參數而有所不同
  commentUrl = requests.get(f'https://today.line.me/webapi/comment/list?articleId={id}&sort=POPULAR&direction=DESC&country=TW&limit=30&pivot={n}&postType=Article')
  json = commentUrl.json()     # 取得對應網址的 json 內容
  comments = json['result']['comments']['comments']   # 取得該網址下所有留言
  for i in comments :
    try:
        print('<' + i['displayName'] + '>\n' + i['contents'][0]['extData']['content'])
        print('----------------')
    except:
        pass
for i in range(0, num, 30):
    getC(i)