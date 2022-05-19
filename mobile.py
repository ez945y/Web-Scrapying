from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    email = os.getenv('email')
    password = os.getenv('password')
    ser = Service('.\chromedriver.exe')
    op = webdriver.ChromeOptions()
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
    driver.get('https://www.mobile01.com/')
    sleep(2)
    loginBtn = driver.find_element_by_css_selector('a.c-login')
    loginBtn.click()

    sleep(0.5)     # 按下按鈕後，等待 0.5 秒等待頁面開啟
    regEmail = driver.find_element_by_css_selector('#regEmail')
    regEmail.send_keys(email)        # 取得 email 欄位
    regPassword = driver.find_element_by_css_selector('#regPassword')
    regPassword.send_keys(password)
    driver.find_element_by_css_selector('#submitBtn').click()
    sleep(2)
    body = driver.find_element_by_css_selector('body')   # 取得 body
    body.screenshot('./a1.png') 