import requests
import json
import re
if __name__ == '__main__':
    CDCApi = 'https://covid19dashboard.cdc.gov.tw/dash3'
    resp = requests.get(CDCApi)
    json_resp = json.loads(resp.text)
    print(json_resp['0']['昨日確診'])

    regex = re.findall('"昨日確診":(\d+),',resp.text)
    print(regex[0])