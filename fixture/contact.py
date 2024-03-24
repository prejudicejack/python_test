from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import time
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_in_contact_info(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element(By.XPATH, "//div[@class='left']/input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()
        time.sleep(3)
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element(By.XPATH, "//div[@class='left']/input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()
        time.sleep(3)
        self.contact_cache = None

    def delete_contact_by_name(self, selected_contact):
        wd = self.app.wd
        self.open_home_page()
        # select contact by First name and Last name
        self.select_contact_by_title(selected_contact)
        wd.find_element(By.XPATH, "//div[@class='left']/input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()
        time.sleep(3)
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, "//form[@name='MainForm']/input[@onclick='MassSelection()']").click()
        wd.find_element(By.XPATH, "//div[@class='left']/input[@onclick='DeleteSel()']").click()
        wd.switch_to.alert.accept()
        time.sleep(3)
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements(By.XPATH, "//a/img[@title='Edit']")[index].click()
        self.fill_in_contact_info(contact)
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, "//*[@id='%s']/../..//*[@title='Edit']" % id).click()
        self.fill_in_contact_info(contact)
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements(By.XPATH, "//a/img[@title='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements(By.XPATH, "//a/img[@title='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        home_phone = wd.find_element(By.NAME, "home").get_attribute("value")
        mobile_phone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        work_phone = wd.find_element(By.NAME, "work").get_attribute("value")
        phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email1 = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(first_name=first_name, lastname=lastname, id=id, home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2, address=address,
                       email1=email1, email2=email2, email3=email3)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

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

    def contact_count(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def contact_by_title_count(self, first_name, lastname):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
        return len(wd.find_elements(By.XPATH,
                                    "//input[@title='Select (" + first_name + " " + lastname + ")']"))

    def open_home_page(self):
        wd = self.app.wd
        if not ((wd.current_url.endswith("/index.php")) or (wd.current_url.endswith("addressbook/"))):
            wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.XPATH,
                                            "//form[@name='MainForm']/table[@id = 'maintable']/tbody/tr[@name='entry']"):
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                first_name = element.find_element(By.XPATH, "td[3]").text
                lastname = element.find_element(By.XPATH, "td[2]").text
                all_phones = element.find_element(By.XPATH, "td[6]").text
                all_emails = element.find_element(By.XPATH, "td[5]").text
                address = element.find_element(By.XPATH, "td[4]").text
                self.contact_cache.append(Contact(lastname=lastname, first_name=first_name, id=id,
                                                  all_phones_from_homepage=all_phones, address=address,
                                                  all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)
