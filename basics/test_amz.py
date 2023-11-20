import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.mark.smoke
def test_launch():
    driver.get('https://www.myntra.com/')
    driver.maximize_window()

@pytest.mark.smoke
def test_myttile():
    print(driver.title)
@pytest.mark.smoke
def test_mycurrenturl():
    print(driver.current_url)

