import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.page_source)
    driver.maximize_window()
    driver.close()
    #close will always close the current tab
    time.sleep(10)

def test_open_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.page_source)
    driver.maximize_window()
    driver.refresh()
    driver.quit()
    #Quit will always close all the tabs
    time.sleep(10)

