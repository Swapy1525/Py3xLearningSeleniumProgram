from selenium import webdriver
def test_simpletest():
    driver = webdriver.Edge()
    driver.get("http://google.com")
    assert driver.current_url == "https://www.google.com/"

    