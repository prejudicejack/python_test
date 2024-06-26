from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements(By.LINK_TEXT, 'new')) > 0):
            wd.find_element(By.LINK_TEXT, 'groups').click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_in_group_info(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        self.submit_group_deletion()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        self.submit_group_deletion()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_title(self, selected_group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_title(selected_group)
        self.submit_group_deletion()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_all_groups()
        self.submit_group_deletion()
        self.return_to_groups_page()
        self.group_cache = None

    def submit_group_deletion(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "delete").click()

    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "edit").click()

    def modify_first_group_by_index(self, group):
        self.modify_group_by_index(0, group)

    def modify_group_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        self.open_modification_form()
        # change data in fields
        self.fill_in_group_info(group)
        self.submit_form_update()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        self.open_modification_form()
        # change data in fields
        self.fill_in_group_info(group)
        self.submit_form_update()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_all_fields_in_group_selected_by_title(self, group, selected_group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_title(selected_group)
        self.open_modification_form()
        # change data in fields
        self.fill_in_group_info(group)
        self.submit_form_update()
        self.return_to_groups_page()
        self.group_cache = None

    def submit_form_update(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "update").click()

    def select_group_by_title(self, selected_group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='content']/form/span/input[@title='Select ("
                        + selected_group.name + ")']").click()

    def select_all_groups(self):
        wd = self.app.wd
        checkboxes = wd.find_elements(By.XPATH, "//input[@type='checkbox']")
        for checkbox in checkboxes:
            checkbox.click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def fill_in_group_info(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def group_by_title_count(self, selected_group):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.XPATH, "//div[@id='content']/form/span/input[@title='Select ("
                                    + selected_group + ")']"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
