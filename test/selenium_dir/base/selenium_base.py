from unittest import TestCase
from selenium import webdriver
from time import sleep as sleep
from app.settings import BASE_DIR
from selenium_dir.base.settings import admin_address, username, password, client_address
from selenium_dir.locators.admin_main_locators import admin_username_input_locator, admin_password_input_locator, \
  admin_panel_logout_locator, main_page_locator
from test.selenium_dir.base.settings import driver_name


class SeleniumAdminTest(TestCase):
  def setUp(self):
    self.w = webdriver.Chrome(BASE_DIR + "/test/selenium_dir/selenium_webdriver/" + driver_name)

    # go to admin site
    self.w.get(admin_address)
    sleep(1.5)

    # log in
    e = self.w.find_element(*admin_username_input_locator)
    e.send_keys(username)
    e = self.w.find_element(*admin_password_input_locator)
    e.send_keys(password)
    e.submit()
    sleep(1.5)

    assert "login" not in self.w.current_url

  def tearDown(self):
    self.w.find_element(*main_page_locator)
    self.w.find_element(*admin_panel_logout_locator).click()
    sleep(1.5)
    assert "Wylogowany" in self.w.page_source
    self.w.quit()


class SeleniumClientTest(TestCase):
  def setUp(self):
    self.w = webdriver.Chrome(BASE_DIR + "/test/selenium_dir/selenium_webdriver/" + driver_name)
    self.w.get(client_address)
    sleep(1.5)

  def tearDown(self):
    self.w.quit()
