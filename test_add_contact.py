# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wdcontact = webdriver.Firefox()
        self.wdcontact.implicitly_wait(30)

    def test_add_contact(self):
        wdcontact = self.wdcontact
        self.open_homepage(wdcontact)
        self.login(wdcontact, username="admin", password="secret")
        self.contact_creation(wdcontact, Contact(first_name="FN1", middle_name="MN1", last_name="LN1", nickname="NN1",email="EM1"))
        self.return_homepage(wdcontact)
        self.logout(wdcontact)

    def logout(self, wdcontact):
        wdcontact.find_element_by_link_text("Logout").click()

    def return_homepage(self, wdcontact):
        wdcontact.find_element_by_link_text("home page").click()

    def contact_creation(self, wdcontact, Contact):
        # Init contact creation
        wdcontact.find_element_by_link_text("add new").click()
        # Fullfill contact form
        wdcontact.find_element_by_name("firstname").click()
        wdcontact.find_element_by_name("firstname").clear()
        wdcontact.find_element_by_name("firstname").send_keys(Contact.first_name)
        wdcontact.find_element_by_name("middlename").clear()
        wdcontact.find_element_by_name("middlename").send_keys(Contact.middle_name)
        wdcontact.find_element_by_name("lastname").clear()
        wdcontact.find_element_by_name("lastname").send_keys(Contact.last_name)
        wdcontact.find_element_by_name("nickname").clear()
        wdcontact.find_element_by_name("nickname").send_keys(Contact.nickname)
        wdcontact.find_element_by_name("email").click()
        wdcontact.find_element_by_name("email").clear()
        wdcontact.find_element_by_name("email").send_keys(Contact.email)
        # Submit contact creation
        wdcontact.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wdcontact, username, password):
        wdcontact.find_element_by_name("user").click()
        wdcontact.find_element_by_name("user").clear()
        wdcontact.find_element_by_name("user").send_keys(username)
        wdcontact.find_element_by_name("pass").clear()
        wdcontact.find_element_by_name("pass").send_keys(password)
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
