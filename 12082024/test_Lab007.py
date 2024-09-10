import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import allure
import pytest


@pytest.mark.positive
@allure.title("TC1 verify that login page is open")
@allure.description(
    "Verify that url changes when we select make appointment button_ mini project 1")
def test_mini_project_1():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # find the element the anchor tag
    # we need to find the unique attribute which can find the web element.
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")

    # click on it
    make_appointment_element.click()

    #verify the updated URL
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(10)
    driver.quit()

