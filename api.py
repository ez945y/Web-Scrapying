import requests
import json

if __name__ == '__main__':
    result_list = []
    catime = int(input("請輸入要取得幾張貓咪圖片 : "))
    for _ in range(catime):
        url = 'https://covid19dashboard.cdc.gov.tw/dash3'
        resp = requests.get(url)
        json_resp = json.loads(resp.text)
        result_list.append(json_resp['url'])
    with open('C:\\Users\\admin\\De1sktop\\visual env\\庫Cat_images.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, indent=2,
                  sort_keys=True, ensure_ascii=False)