from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(chrome_options=option)
    results = []
    driver = webdriver.Chrome()
    driver.get('https://www.dcard.tw/f')
    sleep(2)
    eles = driver.find_elements(By.CLASS_NAME,value="tgn9uw-3")
    for ele in eles:
        result = {}
        title = ele.find_element(By.CLASS_NAME,value="tgn9uw-3").text
        href = ele.find_element(By.CLASS_NAME,value="tgn9uw-3").get_attribute('href')
        subtitle = ele.find_element(By.CLASS_NAME,value='tgn9uw-4').text
        result = {
            'title': title,
            'href': href,
            'subtitle': subtitle
        }
        results.append(result)
    print(results)
    with open('Dcard-articles.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2,
                  sort_keys=True, ensure_ascii=False)