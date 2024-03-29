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

class TestAddannouncement():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addannouncement(self):
    self.driver.get("http://172.20.10.3/")
    self.driver.set_window_size(697, 714)
    self.driver.find_element(By.LINK_TEXT, "Teacher").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-signup").click()
    self.driver.find_element(By.ID, "first_name").click()
    self.driver.find_element(By.ID, "first_name").click()
    self.driver.find_element(By.ID, "first_name").send_keys("Ahmed")
    self.driver.find_element(By.ID, "last_name").click()
    self.driver.find_element(By.ID, "last_name").send_keys("salem")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > .control-label").click()
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").send_keys("ahmed.husu@gmail.com")
    self.driver.find_element(By.ID, "last_name").click()
    self.driver.find_element(By.ID, "last_name").click()
    element = self.driver.find_element(By.ID, "last_name")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").click()
    element = self.driver.find_element(By.ID, "Email")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "Email").send_keys("ahmed.salem@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123456789")
    self.driver.find_element(By.ID, "type").click()
    self.driver.find_element(By.ID, "type").click()
    dropdown = self.driver.find_element(By.ID, "type")
    dropdown.find_element(By.XPATH, "//option[. = 'Teacher']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").send_keys("ahmed.husu@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".alert")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").click()
    element = self.driver.find_element(By.ID, "Email")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "Email").send_keys("ahmed.salem@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123456789")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "ShowCourses").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.close()
  
