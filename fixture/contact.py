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
        self.change_contact_info("firstname", contact.first_name)
        self.change_contact_info("middlename", contact.middlename)
        self.change_contact_info("lastname", contact.lastname)
        self.change_contact_info("nickname", contact.nickname)
        # self.change_contact_info("photo", "C:\\fakepath\\last-post1.jpg")
        self.change_contact_info("title", contact.title)
        self.change_contact_info("company", contact.company)
        self.change_contact_info("address", contact.address)
        self.change_contact_info("home", contact.home_phone)
        self.change_contact_info("mobile", contact.mobile_phone)
        self.change_contact_info("work", contact.work_phone)
        self.change_contact_info("fax", contact.fax)
        self.change_contact_info("email", contact.email1)
        self.change_contact_info("email2", contact.email2)
        self.change_contact_info("email3", contact.email3)
        self.change_contact_info("homepage", contact.homepage)
        self.change_contact_info_dropdown_field("bday", contact.birthday_day)
        self.change_contact_info_dropdown_field("bmonth", contact.birthday_month)
        self.change_contact_info("byear", contact.birthday_year)
        self.change_contact_info_dropdown_field("aday", contact.anniversary_day)
        self.change_contact_info_dropdown_field("amonth", contact.anniversary_month)
        self.change_contact_info("ayear", contact.anniversary_year)
        self.change_contact_info("address2", contact.address2)
        self.change_contact_info("phone2", contact.phone2)
        self.change_contact_info("notes", contact.notes)

    def change_contact_info(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_contact_info_dropdown_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)
            # wd.find_element(By.NAME, field_name).click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()
