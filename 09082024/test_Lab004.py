import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwlogin():
    # option class -
    # customize the browser behaviour during automated testing
    #Chrome -> headless mode no UI (fast)- execution will happen
    # disable gpu, add extension, maximize,set window

    # create an instance of chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    time.sleep(10)

