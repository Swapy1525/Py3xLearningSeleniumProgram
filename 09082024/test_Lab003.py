import time

from selenium import webdriver

def test_open_vwlogin():
    driver = webdriver.Chrome()
    # driver = webdriver.edge()
    # code is sent as a an HTTP request
    # post request - sesssion id created - 8ce566543954cf38af2de16505c7d0cb- 16 digit
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"

    print(driver.session_id)
    time.sleep(10)


