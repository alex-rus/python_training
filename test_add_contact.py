# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wdcontact = webdriver.Firefox()
        self.wdcontact.implicitly_wait(30)

    def test_add_contact(self):
        wdcontact = self.wdcontact
        self.open_homepage(wdcontact)
        self.login(wdcontact)
        self.contact_creation(wdcontact)
        self.return_homepage(wdcontact)
        self.logout(wdcontact)

    def logout(self, wdcontact):
        wdcontact.find_element_by_link_text("Logout").click()

    def return_homepage(self, wdcontact):
        wdcontact.find_element_by_link_text("home page").click()

    def contact_creation(self, wdcontact):
        # Init contact creation
        wdcontact.find_element_by_link_text("add new").click()
        # Fullfill contact form
        wdcontact.find_element_by_name("firstname").click()
        wdcontact.find_element_by_name("firstname").clear()
        wdcontact.find_element_by_name("firstname").send_keys("First_name4")
        wdcontact.find_element_by_name("middlename").clear()
        wdcontact.find_element_by_name("middlename").send_keys("Middle_name4")
        wdcontact.find_element_by_name("lastname").clear()
        wdcontact.find_element_by_name("lastname").send_keys("Last_name5")
        wdcontact.find_element_by_name("nickname").clear()
        wdcontact.find_element_by_name("nickname").send_keys("NIckname6")
        wdcontact.find_element_by_name("email").click()
        wdcontact.find_element_by_name("email").clear()
        wdcontact.find_element_by_name("email").send_keys("email6")
        # Submit contact creation
        wdcontact.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wdcontact):
        wdcontact.find_element_by_name("user").click()
        wdcontact.find_element_by_name("user").clear()
        wdcontact.find_element_by_name("user").send_keys("admin")
        wdcontact.find_element_by_name("pass").clear()
        wdcontact.find_element_by_name("pass").send_keys("secret")
        wdcontact.find_element_by_id("LoginForm").submit()

    def open_homepage(self, wdcontact):
        wdcontact.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wdcontact.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wdcontact.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wdcontact.quit()

if __name__ == "__main__":
    unittest.main()
