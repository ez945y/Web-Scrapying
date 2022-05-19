from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from dotenv import load_dotenv
import os
load_dotenv()
email = os.getenv('email')
password = os.getenv('password')
header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
ser = Service('.\chromedriver.exe')
op = webdriver.ChromeOptions()
op.add_argument('--headless')
op.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
op.add_experimental_option('useAutomationExtension', False)
op.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
driver=webdriver.Chrome(service=ser,options=op)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.maximize_window()
driver.get('https://tpsr.forest.gov.tw/TPSOrder/wSite/index.do?action=indexPage#')
sleep(2)
driver.execute_script(f'window.scrollTo(0,200)')
driver.find_element_by_css_selector('a[href="/login"]').click()
sleep(2)
username = driver.find_element_by_css_selector('input[autocomplete="username"]')
username.send_keys(email)
print('輸入 email 完成')
buttons = driver.find_elements_by_css_selector('div[role="button"]')
for bt in buttons:
    if bt.text == '下一步' or bt.text == 'Next':
        bt.click()
        print('點擊下一步')
        break
sleep(2)
try:
    driver.find_element_by_css_selector('input[autocomplete="on"]').send_keys('ez945y')
    buttons = driver.find_elements_by_css_selector('div[role="button"]')
    for bt in buttons:
        if bt.text == '下一步' or bt.text == 'Next':
            bt.click()  
            print('驗證使用者帳號，點擊下一步')
            break
    sleep(2)      
except:
    print('ok')
    sleep(2) 
driver.find_element_by_css_selector('input[autocomplete="current-password"]').send_keys(password)
print('輸入密碼')
buttons = driver.find_elements_by_css_selector('div[role="button"]')
for i in buttons:
    if i.text == '登入' or i.text == 'Log in':
        i.click()
        print('點擊登入')
        break
sleep(2)
textbox = driver.find_element_by_css_selector('div[role="textbox"]')
textbox.send_keys('Hello World!I am Robot3~ ^_^')
print('輸入文字')
sleep(1)
#imgInput = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]')
#imgInput.send_keys('C:\\Users\\admin\\Desktop\\S__38821892.jpeg')
#print('上傳圖片')
#sleep(1)
buttons = driver.find_elements_by_css_selector('div[role="button"]')
for i in buttons:
  if i.text == '推文' or i.text == 'Tweet':
    i.click()
    print('推文完成')
    break


