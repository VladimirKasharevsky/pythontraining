class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        # Fill contact info
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/label").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.mail)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def edit_first_contact(self):
        wd = self.app.wd
        # Open edit page of first contact
        wd.find_element_by_xpath("//td[@class = 'center' and ./a][2]").click()

    def edit(self, new_contact_data):
        wd = self.app.wd
        # Fill contact info
        wd = self.fill_contact_form(new_contact_data)
        # Submit contact edition
        self.submit_editins()
        self.return_to_home_page()

    def submit_editins(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='update'][2]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.mail)

    def count(self):
        wd = self.app.wd
        self.open_add_contact_page()
        return len(wd.find_elements_by_name("selected[]"))


