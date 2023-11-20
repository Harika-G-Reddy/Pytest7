import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pytest_html_reporter import attach

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

attach(data=driver.get_screenshot_as_png())

@pytest.mark.regression
def test_launch():
    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    driver.find_element(By.XPATH,'//input[@id="twotabsearchtextbox"]').send_keys("iphone")
    driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]').click()
    assert "Amazon.in : ipone"==driver.title ,"failed due to product not found"

@pytest.mark.regression
def test_myttile():
    print(driver.title)
@pytest.mark.regression
def test_mycurrenturl():
    print(driver.current_url)

