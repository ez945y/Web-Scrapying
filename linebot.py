import requests

radar_url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0058-003?Authorization=rdec-key-123-45678-011121314&format=JSON'
radar = requests.get(radar_url)        # 爬取資料
radar_json = radar.json()              # 使用 JSON 格式
radar_img = radar_json['cwbopendata']['dataset']['resource']['uri']  # 取得圖片網址
radat_time = radar_json['cwbopendata']['dataset']['time']['obsTime']  
print(radar_img)

url = 'https://notify-api.line.me/api/notify'
token = 'qsLZ1IUioqrml59LH94PciJjIxxPVfw4bXMM1WgEffS'
headers = {
    'Authorization': 'Bearer ' + token           # POST 使用的 headers
}
data = {
    'message':'從雷達回波看看會不會下雨～',   # 發送的訊息
    'imageThumbnail':radar_img+'?'+radat_time,          # 預覽圖網址
    'imageFullsize':radar_img+'?'+radat_time            # 完整圖片網址
}
data = requests.post(url, headers=headers, data=data)
