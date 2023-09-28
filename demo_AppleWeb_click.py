import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="module")
def chrome_driver():
  print('Setup start')
  driver = webdriver.Chrome()
  vars = {}
  driver.implicitly_wait(5)
  print('Setup End')

  yield driver
  print('teardown() start')
  driver.quit()
  print('teardown() end')


def test_1_title_chk(chrome_driver):
  print('test_case_1 start')
  chrome_driver.get("https://www.apple.com/")
  chrome_driver.set_window_size(1900, 1020)
  chrome_driver.find_element(By.ID, "ac-ls-continue").click()
  time.sleep(2)
  assert "Apple (台灣)" in chrome_driver.title
  print('test_case_1 end')

def test_2_keyword_chk(chrome_driver):  
  print('test_case_2 start')
  chrome_driver.find_element(By.LINK_TEXT, "尋找直營店").click()
  time.sleep(2)
  chrome_driver.find_element(By.CSS_SELECTOR, ".store-card-wrapper:nth-child(1) .store-name").click()
  time.sleep(2)
  elements = chrome_driver.find_elements(By.XPATH, "//h2[contains(.,\'我們能如何幫助你？\')]")
  assert len(elements) > 0
  print('test_case_2 end')