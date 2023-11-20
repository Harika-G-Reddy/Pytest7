import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

@pytest.mark.parametrize("items,expectdevalue",[("Iphone","Amazon.in : iphone"),("Oppo","Amazon.in : Oppo"),("Vivo","Amazon.in : Vivo")])
def test_launch(items,expectdevalue):
    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    driver.find_element(By.XPATH,'//input[@id="twotabsearchtextbox"]').send_keys(items)
    driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]').click()
    assert expectdevalue==driver.title ,"failed due to product not found"
