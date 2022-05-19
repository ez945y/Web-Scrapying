from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.pinterest.com/astrologcy/nail-inspo/nails/')
imgCount = driver.find_element_by_css_selector('div[data-test-id="pin-count"]')
count = int(imgCount.text.split(' ')[0])    # 拆分字串，取出前方的數字
print(count)   

imgList=[]
scroll = 0
def getI():
    global imgList, scroll
    scroll += 450
    driver.execute_script(f'window.scroll(0,{scroll})')
    sleep(0.5)
    img = driver.find_elements_by_css_selector('div[data-test-id="pin-count"]')
    for i in img:
        try:
            url = i.get_attribute('src')
            if url not in imgList and len(imgList)<count:
                imgList.append(url)
        except:
            continue
while True:
    getI()
    if len(imgList)>= 1:
        break
print(imgList)