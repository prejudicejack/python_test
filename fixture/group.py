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
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def delete_group_by_title(self, selected_group):
        wd = self.app.wd
        self.open_groups_page()
        # select group by title
        self.select_group_by_title(selected_group)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        # select group by title
        self.select_all_groups()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # open selected group page for edition
        wd.find_element(By.NAME, "edit").click()
        # change data in fields
        self.fill_in_group_info(group)
        # submit update
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def edit_group_by_title(self, group, selected_group):
        wd = self.app.wd
        self.open_groups_page()
        # select group by title
        self.select_group_by_title(selected_group)
        # open selected group page for edition
        wd.find_element(By.NAME, "edit").click()
        # change data in fields
        self.fill_in_group_info(group)
        # submit update
        wd.find_element(By.NAME, "update").click()
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

    def fill_in_group_info(self, group):
        wd = self.app.wd
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()
