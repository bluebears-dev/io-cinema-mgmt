from unittest import TestCase
from selenium import webdriver

class SeleniumTest(TestCase):
  def setUp(self):
    self.w = webdriver.Chrome("selenium_webdriver/chromedriver")

  def tearDown(self):
    self.w.quit()
