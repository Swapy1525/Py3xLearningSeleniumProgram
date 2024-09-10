import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pytest
import allure



@pytest.mark.positive
@allure.title("TC2 verify that with invalid Email ,Password ,Error message is displayed")
@allure.description(
"verify that with invalid Email ,Password ,Error message is displayed")

def test_mini_project_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"

    email_webelement = driver.find_element(By.ID,"login-username")
    email_webelement.send_keys("admin@admin.com")

    # <input type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe">

    pass_webelement = driver.find_element(By.CSS_SELECTOR,"[data-qa='jobodapuxe']")
    pass_webelement.send_keys("admin@123")

    #     <input type="email"
    #     class="text-input W(100%)"
    #     name="username"
    #     id="login-username"
    #     data-qa="hocewoqisi">
    #  if id is unavailable find element by name By.NAME
    # css selector - custom attribute [] data-qa=

    submit_btn_web_element = driver.find_element(By.ID,"js-login-btn")
    submit_btn_web_element.click()

    time.sleep(3)   #super bad practice - python interpretor to stop -
    #webdriver should stop for the element


    error_message = driver.find_element(By.ID,"js-notification-box-msg")
    assert error_message.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
    driver.quit()















    
