import time

import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_mini_project_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"

    sign_up_tab = driver.find_element(By.LINK_TEXT,"Start a free trial")
    sign_up_tab.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(5)

    driver.quit()







