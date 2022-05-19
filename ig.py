from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    account = os.getenv('account')
    password = os.getenv('password')
    ser = Service('.\chromedriver.exe')
    op = webdriver.ChromeOptions()
    op.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    op.add_experimental_option('useAutomationExtension', False)
    op.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
    driver=webdriver.Chrome(service=ser,options=op)
    driver.maximize_window()
    driver.get('https://www.instagram.com')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(account)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
    sleep(3)
    driver.get('https://www.instagram.com/prerequisiteofdelight/')
    eles = driver.find_elements_by_class_name('_9AhH0')
    for ele in eles:
        ele.click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
        sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/button').click()
        sleep(1)
        break
    body = driver.find_element_by_css_selector('body')   # 取得 body
    body.screenshot('./a1.png') 