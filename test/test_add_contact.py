from model.contact import Contact


def test_add_contacts(app):
    app.contact.open_add_contact_page()
    app.contact.create(Contact(name="pyt", last_name="pyt", company_name="pyt", address="pyt", mail="pyt@pyt.py"))

