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

class TestAddcourseSucceded():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addcourseSucceded(self):
    self.driver.get("http://172.20.10.3/")
    self.driver.set_window_size(697, 714)
    self.driver.find_element(By.LINK_TEXT, "Student").click()
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").send_keys("ahmed.muhammed11a@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("12345678899")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123456789")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()
    self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#EnrollCourse form").click()
    self.driver.find_element(By.ID, "course_id").click()
    element = self.driver.find_element(By.ID, "course_id")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "course_id").click()
    self.driver.find_element(By.ID, "course_id").click()
    self.driver.find_element(By.ID, "course_id").click()
    self.driver.find_element(By.ID, "course_id").send_keys("Cs103")
    self.driver.find_element(By.ID, "course_id").send_keys("Cs101")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").click()
    self.driver.find_element(By.LINK_TEXT, "Courses").click()
    self.driver.find_element(By.LINK_TEXT, "Cs101").click()
    self.driver.close()
  
