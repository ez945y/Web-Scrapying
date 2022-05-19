import requests
import json

if __name__ == '__main__':
    resp = requests.get('https://www.dcard.tw/service/api/v2/posts')
    json_resp = json.loads(resp.text)
    with open('C:\\Users\\admin\\Desktop\\visual env\\庫\\Dcard_articles.json', 'w', encoding='utf-8') as f:
        json.dump(json_resp, f, indent=2,
                  sort_keys=True, ensure_ascii=False)