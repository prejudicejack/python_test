# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestCreateContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_create_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.create_contact(wd,
                            first_name="Lucy",
                            middlename="Michelle",
                            lastname="Sunrise",
                            nickname="Lu",
                            title="Title1",
                            company="Company",
                            address="street Company",
                            home_phone="9998999",
                            mobile_phone="7654",
                            work_phone="123234",
                            fax="567456",
                            email1="some@mail.com",
                            email2="next@mail.com",
                            email3="onemore@mail.com",
                            homepage="https://somepage.com",
                            birthday_day="30",
                            birthday_month="October",
                            birthday_year="1978",
                            anniversary_day="10",
                            anniversary_month="November",
                            anniversary_year="2000",
                            selected_group="2",
                            address2="some street next",
                            phone2="12",
                            notes="sun")
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create_contact(self, wd, first_name, middlename, lastname, nickname, title, company, address, home_phone,
                       mobile_phone, work_phone, fax, email1, email2, email3, homepage, birthday_day, birthday_month,
                       birthday_year, anniversary_day, anniversary_month, anniversary_year, selected_group, address2,
                       phone2, notes):
        # open new contact page
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill in form
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(first_name)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(nickname)
        # wd.find_element(By.NAME, "photo").click()
        # wd.find_element(By.NAME, "photo").clear()
        # wd.find_element(By.NAME, "photo").send_keys("C:\\fakepath\\last-post1.jpg")
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(address)
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(home_phone)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(mobile_phone)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(work_phone)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(email1)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(homepage)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(birthday_day)
        wd.find_element(By.XPATH, "//option[@value='" + birthday_day + "']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(birthday_month)
        wd.find_element(By.XPATH, "//option[@value='" + birthday_month + "']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(birthday_year)
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(anniversary_day)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[@value='" + anniversary_day + "']").click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(anniversary_month)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[@value='" + anniversary_month + "']").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(anniversary_year)
        wd.find_element(By.NAME, "new_group").click()
        Select(wd.find_element(By.NAME, "new_group")).select_by_visible_text(selected_group)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[5]/option[text()='" + selected_group + "']").click()
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(address2)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(phone2)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(notes)
        # submit contact creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def login(self, wd, user_name, password):
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(user_name)
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
