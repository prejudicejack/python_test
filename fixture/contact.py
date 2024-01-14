from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # open new contact page
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill in form
        self.fill_in_contact_info(contact)
        # submit contact creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # open home page
        wd.find_element(By.LINK_TEXT, "home").click()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//div[@class='left']/input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()

    def delete_contact_by_name(self, selected_contact):
        wd = self.app.wd
        # open home page
        wd.find_element(By.LINK_TEXT, "home").click()
        # select contact by First name and Last name
        self.select_contact_by_title(selected_contact)
        # submit deletion
        wd.find_element(By.XPATH, "//div[@class='left']/input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()

    def delete_all_contacts(self):
        wd = self.app.wd
        # open home page
        wd.find_element(By.LINK_TEXT, "home").click()
        # select all contacts
        wd.find_element(By.XPATH, "//form[@name='MainForm']/input[@onclick='MassSelection()']").click()
        # submit deletion
        wd.find_element(By.XPATH, "//div[@class='left']/input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # open home page
        wd.find_element(By.LINK_TEXT, "home").click()
        # modify first contact
        wd.find_element(By.XPATH, "//a/img[@title='Details']").click()
        wd.find_element(By.NAME, "modifiy").click()
        # fill in form
        self.fill_in_contact_info(contact)
        # submit contact updating
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()

    def select_contact_by_title(self, selected_contact):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//input[@title='Select (" + selected_contact.first_name + " " + selected_contact.lastname + ")']").click()

    def fill_in_contact_info(self, contact):
        wd = self.app.wd
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.first_name)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        # wd.find_element(By.NAME, "photo").click()
        # wd.find_element(By.NAME, "photo").clear()
        # wd.find_element(By.NAME, "photo").send_keys("C:\\fakepath\\last-post1.jpg")
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home_phone)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work_phone)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email1)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.birthday_day)
        wd.find_element(By.XPATH, "//select[1]/option[text()='" + contact.birthday_day + "']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.birthday_month)
        wd.find_element(By.XPATH, "//select[2]/option[text()='" + contact.birthday_month + "']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.birthday_year)
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element(By.XPATH, "//select[3]/option[text()='" + contact.anniversary_day + "']").click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element(By.XPATH, "//select[4]/option[text()='" + contact.anniversary_month + "']").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.anniversary_year)
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()
