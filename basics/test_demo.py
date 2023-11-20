import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
@pytest.mark.regression
@pytest.mark.order(1)
def test_launch():
    driver.get('https://demoblaze.com/')
    driver.maximize_window()
@pytest.mark.regression
@pytest.mark.order(3)
def test_title():
    print(driver.title)
@pytest.mark.regression
@pytest.mark.order(2)
def test_currenturl():
    print(driver.current_url)
@pytest.mark.regression
@pytest.mark.order(4)
def test_login():
    driver.find_element(By.XPATH,'//a[@id="login2"]').click()
