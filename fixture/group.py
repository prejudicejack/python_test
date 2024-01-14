from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
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

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        self.submit_group_deletion()
        self.return_to_groups_page()

    def delete_group_by_title(self, selected_group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_title(selected_group)
        self.submit_group_deletion()
        self.return_to_groups_page()

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_all_groups()
        self.submit_group_deletion()
        self.return_to_groups_page()

    def submit_group_deletion(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "delete").click()

    def edit_all_fields_in_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        self.open_modification_form()
        # change data in fields
        self.fill_in_group_info(group)
        self.submit_form_update()
        self.return_to_groups_page()

    def edit_all_fields_in_group_selected_by_title(self, group, selected_group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_title(selected_group)
        self.open_modification_form()
        # change data in fields
        self.fill_in_group_info(group)
        self.submit_form_update()
        self.return_to_groups_page()

    def select_group_by_title(self, selected_group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='content']/form/span/input[@title='Select ("
                        + selected_group.name + ")']").click()

    def select_all_groups(self):
        wd = self.app.wd
        checkboxes = wd.find_elements(By.XPATH, "//input[@type='checkbox']")
        for checkbox in checkboxes:
            checkbox.click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        self.open_modification_form()
        # change data in fields
        self.fill_in_group_info(new_group_data)
        self.submit_form_update()
        self.return_to_groups_page()

    def submit_form_update(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "update").click()

    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "edit").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

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
