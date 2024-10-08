import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import allure
import time

@pytest.mark.positive
def test_mini_project_4():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # make_atm_btn = driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']")
    # make_atm_btn = driver.find_element(By.XPATH,"//a[@href='./profile.php#login']")
    make_atm_btn = driver.find_element(By.CSS_SELECTOR,"#btn-make-appointment")
    make_atm_btn.click()

    time.sleep(5)
    driver.quit()



