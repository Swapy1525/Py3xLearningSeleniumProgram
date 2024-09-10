import time

import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_mini_project_1():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # find the element and anchor tab
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    # select the id
    make_appointment_element.click()

    time.sleep(10)

    driver.quit()
