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

class TestShowingAssignmentsAnnouncementsandquizzes():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_showingAssignmentsAnnouncementsandquizzes(self):
    self.driver.get("http://172.20.10.3/")
    self.driver.set_window_size(697, 714)
    self.driver.find_element(By.LINK_TEXT, "Student").click()
    self.driver.find_element(By.ID, "Email").click()
    self.driver.find_element(By.ID, "Email").send_keys("ahmed.muhammed11a@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("123456789")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()
    self.driver.find_element(By.LINK_TEXT, "Courses").click()
    self.driver.find_element(By.LINK_TEXT, "Cs101").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1) > b").click()
    self.driver.find_element(By.CSS_SELECTOR, "#Announcement4 span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#Announcement5 span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#Announcement1213 span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#Announcement12323 span").click()
    self.driver.close()
  