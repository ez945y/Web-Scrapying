import requests
import re
import json
from bs4 import BeautifulSoup

version_list = ['21.04/', '20.10/', '20.04/', '18.04/', '16.04/', '14.04/']
url = 'http://ftp.ubuntu-tw.org/ubuntu-releases/'
result_dict = {}

for version in version_list:
    r = requests.get(url+version)
    soup = BeautifulSoup(r.text, 'html5lib')
    desktop_iso = soup.find('a', string=re.compile(
        'ubuntu-\d{2}\.\d{2}\.?\d{0,2}-desktop-amd64\.iso'))['href']
    server_iso = soup.find('a', string=re.compile(
        'ubuntu-\d{2}\.\d{2}\.?\d{0,2}(-live)?-server-amd64\.iso'))['href']
    result_dict[version] = {
        "desktop_iso": r.url + desktop_iso,
        "server_iso": r.url + server_iso
    }

with open('iso-image.json', 'w', encoding='utf-8') as f:
    json.dump(result_dict, f, indent=2,
              sort_keys=True, ensure_ascii=False)