# Generated by Selenium IDE
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

class TestLogoutasasuper():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logoutasasuper(self):
    self.driver.get("http://172.20.10.3/")
    self.driver.set_window_size(697, 714)
    self.driver.find_element(By.LINK_TEXT, "Teacher").click()
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").send_keys("ahmed.husu@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123456789")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()
    self.driver.find_element(By.LINK_TEXT, "Signout").click()
    self.driver.close()
  
