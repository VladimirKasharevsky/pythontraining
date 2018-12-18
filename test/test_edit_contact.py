from model.contact import Contact


def test_add_contacts(app):
    app.contact.edit_first_contact()
    app.contact.edit(Contact(name="pytedit", last_name="pytedit", company_name="pytedit", address="pytedit", mail="pytedit@pytedit.py"))